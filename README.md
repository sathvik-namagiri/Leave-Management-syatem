
# 📌 Leave Management System Using FastAPI

A full-stack **Leave Management System** built using **FastAPI (Backend)** and **Streamlit (Frontend)** to efficiently manage employee leave requests, approvals, and tracking.

---

## 🚀 Problem Statement
Managing employee leave manually is often inefficient, error-prone, and lacks transparency. Organizations struggle with tracking requests, approvals, and maintaining accurate records.

This system solves these challenges by providing:

* 🧾 **Centralized Leave Management** – All leave data stored in one system
* ⚡ **Automated Workflow** – Seamless leave application and approval process
* 👨‍💼 **Admin Control** – Approve or reject requests with ease
* 📊 **Real-time Dashboard** – View employee count and leave statistics
* 🔒 **Data Validation & Integrity** – Ensured using Pydantic and ORM models
* 🌐 **API-driven Architecture** – Scalable backend with FastAPI
* 🎯 **User-Friendly Interface** – Simple and interactive UI using Streamlit

---

## 🧩 Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Database:** SQLite / PostgreSQL
* **ORM:** SQLAlchemy
* **Validation:** Pydantic

---

## 📁 Project Structure

```bash
leave-management-system/
│
├── app.py              # Streamlit frontend
├── main.py             # FastAPI backend
├── models.py           # Database models (SQLAlchemy)
├── schemas.py          # Pydantic schemas
├── crud.py             # CRUD operations
├── database.py         # DB connection & session
├── requirements.txt    # Dependencies
```

---

## 🔄 Workflow

1. **Employee Registration**

   * User submits form via Streamlit
   * Data sent to FastAPI
   * Password hashed and stored in DB

2. **Apply Leave**

   * Employee selects dates & reason
   * Request stored as *Pending*

3. **Dashboard**

   * Displays total employees & leave stats

4. **Admin Actions**

   * Approve → Status becomes *Approved*
   * Reject → Status becomes *Rejected*

5. **View Leaves**

   * All leave records displayed in table format

---

## 📊 API Endpoints

| Method | Endpoint              | Description            |
| ------ | --------------------- | ---------------------- |
| POST   | `/register`           | Register employee      |
| POST   | `/apply`              | Apply for leave        |
| GET    | `/leaves`             | Get all leave requests |
| PUT    | `/approve_leave/{id}` | Approve leave          |
| PUT    | `/reject_leave/{id}`  | Reject leave           |


## 💡 Use Cases

* Small to medium companies
* College projects
* HR management prototypes





