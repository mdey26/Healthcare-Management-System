from django.db import models

class Patient(models.Model):
    patient_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact_info = models.CharField(max_length=255)
    allergies = models.TextField(blank=True)
    medical_history = models.TextField(blank=True)
    current_prescriptions = models.TextField(blank=True)
    doctor_notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
