# Healthcare Backend System

This project is a **Django REST Framework (DRF)**-based backend system for a healthcare application.  
It uses **PostgreSQL** as the database, **JWT Authentication** for security, and follows a **RESTful API structure**.  
The system allows **user registration and login**, along with full **CRUD operations** for managing **patients, doctors, and their mappings**.

---

## 📌 Features

- User Registration and Login with **JWT Authentication** (`djangorestframework-simplejwt`)
- **Patient Management** (CRUD) — each user can manage their own patients.
- **Doctor Management** (CRUD) — all authenticated users can access.
- **Patient-Doctor Mapping** — assign doctors to patients, list assignments, and remove mappings.
- **PostgreSQL Database** using Django ORM.
- **Environment Variables** (`.env`) for sensitive settings (database credentials, secret key).
- All sensitive files are **excluded from version control** via `.gitignore`.

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Authentication:** JWT (`djangorestframework-simplejwt`)
- **Database:** PostgreSQL

---

## 📂 Project Structure

- `Healthcare Backend System/`
- `├── healthcare_app/`
- `│ ├── models.py # Custom User & Expense Models`
- `│ ├── serializers.py # DRF Serializers`
- `│ ├── views.py # API Views (Register, Login, Patiend, Doctor, Patent-Doctor mapping)`
- `│ ├── urls.py # App-level Routing`
- `├── healthcare_pro/`
- `│ ├── settings.py # Project Settings`
- `│ ├── urls.py # Main Routing`
- `├── postman_tests/ # Postman collection for testing APIs`
- `├── .env # Environment variables (ignored by Git)`
- `├── .gitignore # To exclude .env and other sensitive files`
- `├── requirements.txt # Python dependencies`
- `├── manage.py # Django entry point`

---

## Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone <your-repo-url>
   cd Healthcare_Backend_System
   
---

 2. **Create and activate a virtual environment**
  ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

3. **Install dependencies**

```bash
pip install -r requirements.txt
```
---

4. **Configure Environment Variables**
Create a .env file in the project root (this file is excluded via .gitignore):

```ini
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```
---

5. **Apply Migrations** 

```bash

python manage.py makemigrations
python manage.py migrate
```
---
6. **Run Server**

```bash

python manage.py runserver
```
---

## API Documentation
All endpoints are prefixed with /api/.
Authentication is required for **patients**, **doctors**, and **mappings APIs** via JWT.

1. ## Authentication APIs
**Register a New User**
POST ```/api/auth/register/```

**Request Body:**

```json

{
    "name": "Ayush",
    "email": "ayush@example.com",
    "password": "123456"
}
```
---

**Response:**

```json
{
    "id": 1,
    "email": "ayush@example.com",
    "token": "eyJhbGciOiJIUzI1..."
}
```
---

**Login User**
**POST** ```/api/auth/login/```

**Request Body:**

```json

{
    "email": "ayush@example.com",
    "password": "123456"
}
```
---

**Response:**

```json
{
    "access": "eyJhbGciOiJIUzI1...",
    "refresh": "eyJhbGciOiJIUzI1..."
}
```
---

Include the access token in headers for subsequent requests:

```makefile
Authorization: Bearer <access_token>
```
---

2. ## Patient Management APIs
Authenticated users can create and manage **only their own patients.**

**Add a Patient**
**POST** ```/api/patients/```

```json

{
    "name": "John Doe",
    "age": 35,
    "gender": "Male",
    "address": "123 Street",
    "phone": "9876543210"
}
```
---

**List All Patients (Created by Authenticated User)**
**GET** ```/api/patients/```

**Get Specific Patient**
**GET** ```/api/patients/<id>/```

**Update Patient**
**PUT** ```/api/patients/<id>/```

```json
{
    "name": "John Smith",
    "age": 36,
    "gender": "Male",
    "address": "456 Avenue",
    "phone": "9876543210"
}
```

---

**Delete Patient**
**DELETE** ```/api/patients/<id>/```

3. Doctor Management APIs
Authenticated users can create, update, or delete doctors.

Add a Doctor
POST /api/doctors/

json
Copy
Edit
{
    "name": "Dr. Alice",
    "specialization": "Cardiologist",
    "email": "alice@example.com",
    "phone": "9876543211"
}
List All Doctors
GET /api/doctors/

Get Specific Doctor
GET /api/doctors/<id>/

Update Doctor
PUT /api/doctors/<id>/

json
Copy
Edit
{
    "name": "Dr. Alice Brown",
    "specialization": "Cardiologist",
    "email": "alicebrown@example.com",
    "phone": "9876543211"
}
Delete Doctor
DELETE /api/doctors/<id>/

4. Patient-Doctor Mapping APIs
Authenticated users can assign doctors to patients, list all mappings, and remove them.

Assign a Doctor to a Patient
POST /api/mappings/

json
Copy
Edit
{
    "patient": 1,
    "doctor": 2
}
List All Mappings
GET /api/mappings/

List Doctors for a Specific Patient
GET /api/mappings/<patient_id>/

Remove a Mapping
DELETE /api/mappings/delete/<id>/

Postman Testing
All tested endpoints are available in the exported Postman collection:

bash
Copy
Edit
/postman_tests/Healthcare_Backend_System.postman_collection.json
You can import this file into Postman to test all APIs with sample requests and responses.

Notes
.env file is ignored in Git for security (.gitignore is configured).

Use Authorization: Bearer <access_token> in headers for all patient, doctor, and mapping APIs.

PostgreSQL must be running, and database credentials should match your .env.

License
This project is for educational and assignment purposes.
Feel free to fork and use it for your own learning.

yaml
Copy
Edit

---

Would you like me to also:
1. **Include screenshots of Postman API responses** (and show how to reference them in the README)?  
2. Or **make this README more professional (with badges, sections like "Tech Stack" and "Contributors")** so it looks portfolio-ready?  
Or **both?** Which do you prefer?







You said:
is it necessary to provide my databse password ?


ChatGPT said:
No, you should never commit your actual database password (or any sensitive credentials) to GitHub.

That’s exactly why we used a .env file and added it to .gitignore.
Here’s what you should do:

What to Commit
In your .env.example (a sample file), include placeholder values like this:

ini
Copy
Edit
SECRET_KEY=your_secret_key_here
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
Commit .env.example (not the real .env), so others know which environment variables they need.

The real .env (with your password) stays only on your machine.

Update README for Security
Instead of asking users to edit .env directly, instruct them like this (update your README’s setup section):

bash
Copy
Edit
cp .env.example .env
# Edit .env and replace placeholder values with your actual credentials
This way:

Reviewers/teammates can run your project without seeing your actual password.

You keep your credentials private.


