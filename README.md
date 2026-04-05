# FinGuard API – Finance Data Processing & Access Control Backend

## 📌 Overview

FinGuard API is a backend system designed to manage financial records with role-based access control. It supports user management, financial data processing, and dashboard analytics.

This project demonstrates backend architecture, API design, data modeling, and access control mechanisms.

---

## ⚙️ Tech Stack

* FastAPI (Backend Framework)
* SQLite (Database)
* SQLAlchemy (ORM)
* Pydantic (Validation)

---

## 🧱 Features

### 👤 User Management

* Create and manage users
* Assign roles (Viewer, Analyst, Admin)
* Activate / deactivate users

### 💰 Financial Records

* Create, update, delete financial records
* Filter records by type and category

### 📊 Dashboard APIs

* Total income
* Total expenses
* Net balance
* Category-wise breakdown
* Recent transactions

### 🔐 Role-Based Access Control

* Viewer → Read-only access
* Analyst → Read + analytics
* Admin → Full access

Access is enforced using dependency-based role checks.

---

## 🔐 Authentication Approach

Authentication is simulated using request headers:

user_id → passed in request header

This allows testing of role-based access without implementing full authentication.

---

## 📡 API Endpoints

### Users

* POST /users
* GET /users
* PATCH /users/{id}

### Records

* POST /records
* GET /records
* PATCH /records/{id}
* DELETE /records/{id}

### Dashboard

* GET /dashboard/summary
* GET /dashboard/category-breakdown
* GET /dashboard/recent

---

## 🧪 How to Run

```bash
git clone https://github.com/YOUR_USERNAME/finguard-backend.git
cd finguard-backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
http://127.0.0.1:8000/docs

---

## 🧪 Testing RBAC

Use header:

user_id: 1  → Admin
user_id: 2  → Analyst
user_id: 3  → Viewer

---

## 📌 Assumptions

* Authentication is simplified using headers
* SQLite is used for simplicity
* Roles are predefined (viewer, analyst, admin)

---

## 🚀 Future Improvements

* JWT-based authentication
* Pagination and search
* Unit testing
* Deployment

---

## 👨‍💻 Author

Aryan Raj