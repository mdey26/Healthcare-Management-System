# 🏥 Healthcare Management System

A full-stack **Django + MongoDB** based healthcare patient management system designed to help hospital staff add, search, update, and delete patient records with ease. Includes user authentication and analytics dashboard with Chart.js visualizations.

---

## 💡 Features

- ✅ Add, View, Edit, Delete Patient Records
- 🔍 Search patients by Name or ID
- 📊 Dashboard with patient statistics (conditions, prescriptions, age)
- 🔒 Admin/Staff Login Authentication
- ⚙️ Access control — only staff can access core features
- 📈 Interactive graphs using Chart.js
- 🌐 Frontend built with HTML, CSS, and JS

---

## ⚙️ Tech Stack

| Layer     | Tech                         |
|-----------|------------------------------|
| Backend   | Django (Python)              |
| Database  | MongoDB (with Djongo)        |
| Frontend  | HTML, CSS, JavaScript        |
| Charts    | Chart.js                     |
| Auth      | Django's built-in auth       |

---

## 🚀 Setup Instructions (For Developers)

### ✅ Step 1: Clone the Repo 

```bash
git clone https://github.com/mdey26/Healthcare-Management-System.git
cd Healthcare-Management-System
```

### ✅ Step 2: Create Virtual Environment (Optional but its recommended)

```bash
python -m venv env
env\Scripts\activate  # for Windows
```

### ✅ Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

### ✅ Step 4: Start MongoDB Locally
```
Ensure MongoDB is running locally at:
mongodb://localhost:27017
```

### ✅ Step 5: Run Migrations 

```bash
python manage.py makemigrations
python manage.py migrate
```

### ✅ Step 6: Create Superuser 

```bash
python manage.py createsuperuser
Put username, email and password which will be used to login into Djanbo admin panel and then to add other users from there. Or in the same way to add other users as well from the bash itself.
```

### ✅ Step 7: Start the Development Server

```bash
python manage.py runserver
```

🧪 Admin Panel Access

Go to this link: http://127.0.0.1:8000/admin
Log in using the superuser account created above.
Add new users and check “Staff status” to give access to core features.


