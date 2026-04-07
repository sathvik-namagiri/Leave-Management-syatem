from sqlalchemy.orm import Session
from models import LeaveRequest, Employee
from datetime import date
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


# ---------------- PASSWORD ----------------
def hash_password(password: str):
    return pwd_context.hash(password.strip())


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# ---------------- EMPLOYEE ----------------
def create_employee(db: Session, emp):
    existing = db.query(Employee).filter(Employee.email == emp.email).first()
    if existing:
        raise ValueError("Email already registered")

    new_emp = Employee(
        name=emp.name,
        email=emp.email,
        password=hash_password(emp.password)
    )

    db.add(new_emp)
    db.commit()
    db.refresh(new_emp)
    return new_emp


def get_employees(db: Session):
    return db.query(Employee).all()


def get_employee_count(db: Session):
    return db.query(Employee).count()


# ---------------- LEAVE ----------------
def create_leave(db: Session, leave):
    if leave.start_date < date.today():
        raise ValueError("Cannot apply for past dates")

    existing = db.query(LeaveRequest).filter(
        LeaveRequest.employee_id == leave.employee_id,
        LeaveRequest.start_date <= leave.end_date,
        LeaveRequest.end_date >= leave.start_date
    ).first()

    if existing:
        raise ValueError("Overlapping leave exists")

    new_leave = LeaveRequest(**leave.dict())
    db.add(new_leave)
    db.commit()
    db.refresh(new_leave)
    return new_leave


# 🔥 UPDATED FUNCTION
def get_leaves(db: Session):
    results = db.query(LeaveRequest, Employee).join(
        Employee, LeaveRequest.employee_id == Employee.id
    ).all()

    leaves = []
    for leave, emp in results:
        leaves.append({
            "id": leave.id,
            "employee_name": emp.name,
            "leave_type": leave.leave_type,
            "start_date": leave.start_date,
            "end_date": leave.end_date,
            "reason": leave.reason,
            "status": leave.status
        })

    return leaves


def update_status(db: Session, leave_id: int, status: str):
    leave = db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()

    if not leave:
        raise ValueError("Leave not found")

    if leave.status != "Pending":
        raise ValueError("Only pending can be updated")

    leave.status = status
    db.commit()
    db.refresh(leave)
    return leave
