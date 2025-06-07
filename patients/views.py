from django.shortcuts import render, redirect
from django.db.models import Count
from .models import Patient
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth.decorators import user_passes_test

def is_staff(user):
    return user.is_authenticated and user.is_staff

@user_passes_test(is_staff)
def add_patient(request):
    if request.method == 'POST':
        patient_id = request.POST['patient_id']
        name = request.POST['name']

        if not patient_id or not name:
            messages.error(request, "Patient ID and Name are required.")
            return render(request, 'patients/add_patient.html')

        if Patient.objects.filter(patient_id=patient_id).exists():
            messages.error(request, "Patient ID already exists.")
            return render(request, 'patients/add_patient.html')

        # Create patient
        Patient.objects.create(
            patient_id=patient_id,
            name=name,
            age=request.POST.get('age'),
            gender=request.POST.get('gender'),
            contact_info=request.POST.get('contact_info'),
            allergies=request.POST.get('allergies'),
            medical_history=request.POST.get('medical_history'),
            current_prescriptions=request.POST.get('current_prescriptions'),
            doctor_notes=request.POST.get('doctor_notes'),
        )
        messages.success(request, "✅ Patient successfully added.")
        return redirect('home_dashboard')

    return render(request, 'patients/add_patient.html')

@user_passes_test(is_staff)
def search_patient(request):
    query = request.GET.get('query')
    patients = []

    if query:
        patients = Patient.objects.filter(
            name__icontains=query
        ) | Patient.objects.filter(
            patient_id__icontains=query
        )

    return render(request, 'patients/search_patient.html', {
        'patients': patients,
        'query': query
    })

def list_patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients/list_patients.html', {'patients': patients})

from django.shortcuts import get_object_or_404

@user_passes_test(is_staff)
def update_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        patient.name = request.POST['name']
        patient.age = request.POST['age']
        patient.gender = request.POST['gender']
        patient.contact_info = request.POST['contact_info']
        patient.medical_history = request.POST['medical_history']
        patient.save()
        return redirect('list_patients')

    return render(request, 'patients/update_patient.html', {'patient': patient})

from django.shortcuts import get_object_or_404, redirect, render

@user_passes_test(is_staff)
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        patient.delete()
        return redirect('list_patients')

    return render(request, 'patients/delete_patient.html', {'patient': patient})

from django.db.models import Count

@user_passes_test(is_staff)  # restrict to staff users
def dashboard(request):
    gender_data = Patient.objects.values('gender').annotate(count=Count('id'))

    labels = [entry['gender'] for entry in gender_data]
    data = [entry['count'] for entry in gender_data]

    return render(request, 'patients/dashboard.html', {
        'labels': labels,
        'data': data
    })

from pymongo import MongoClient
from django.conf import settings

@user_passes_test(is_staff)
def analytics_conditions(request):
    client = MongoClient("mongodb://localhost:27017")
    db = client["healthcare_db"]  # Your DB name from settings.py
    collection = db["patients_patient"]  # Your collection name

    pipeline = [
        {"$group": {"_id": "$medical_history", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]

    results = list(collection.aggregate(pipeline))

    labels = [r["_id"] if r["_id"] else "Unknown" for r in results]
    data = [r["count"] for r in results]

    return render(request, 'patients/analytics_conditions.html', {
        'labels': labels,
        'data': data
    })

@user_passes_test(is_staff)
@login_required
def home_dashboard(request):
    return render(request, 'patients/home_dashboard.html')

# Create your views here.
