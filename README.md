# Study Management System

A simple yet powerful **Django-based Study Management System** designed to manage clinical studies efficiently.  
This project provides CRUD functionality (Create, Read, Update, Delete) with modern UI templates built using **Bootstrap 5**.  
It also includes robust **logging** and **exception handling** for reliability and maintainability.

---

## 🚀 Features

- ✅ Add, Edit, View, and Delete Study records  
- 🎨 Modern responsive UI using **Bootstrap 5**  
- 🧠 Django-based MVC structure  
- 🛡️ Exception handling for safe execution  
- 📜 Centralized logging system for debugging and audits  
- 🔍 CSRF protection for form security  

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Django 5.x |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Database | SQLite3 (default) |
| Logging | Python `logging` module |
| Language | Python 3.10+ |

---

## 📁 Project Structure
```bash
study_mgmt/
│
├── study_mgmt/ 
│ ├── settings.py
│ ├── urls.py 
│ └── wsgi.py 
│
├── studies/ 
│ ├── models.py 
│ ├── views.py 
│ ├── urls.py 
│ ├── forms.py 
│ ├── templates/studies/ 
│ │ ├── study_form.html
│ │ ├── study_view.html
│ │ └── study_list.html
│ └── admin.py 
│
├── static/ 
├── manage.py 
└── README.md
```

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/rubankumarsankar/Student_Management.git
cd Student_Management
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  
```

### 3️⃣ Install Dependencies

```base          
pip install -r requirements.txt

```

### 4️⃣ Run Database Migrations

```base 
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Start the Development Server

```base    
python manage.py runserver

```