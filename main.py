from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Leave Management System")


# ---------------- DB ----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- EMPLOYEE APIs ----------------
@app.post("/employees/register", response_model=schemas.EmployeeResponse, status_code=201)
def register_employee(emp: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_employee(db, emp)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/employees", response_model=list[schemas.EmployeeResponse])
def get_all_employees(db: Session = Depends(get_db)):
    return crud.get_employees(db)


@app.get("/employees/count")
def get_employee_count(db: Session = Depends(get_db)):
    return {"total_employees": crud.get_employee_count(db)}


# ---------------- LEAVE APIs ----------------
@app.post("/apply", response_model=schemas.LeaveResponse, status_code=201)
def apply_leave(leave: schemas.LeaveCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_leave(db, leave)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# 🔥 UPDATED (NO response_model)
@app.get("/leaves")
def get_all(db: Session = Depends(get_db)):
    return crud.get_leaves(db)


@app.put("/approve/{leave_id}")
def approve(leave_id: int, db: Session = Depends(get_db)):
    try:
        return crud.update_status(db, leave_id, "Approved")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put("/reject/{leave_id}")
def reject(leave_id: int, db: Session = Depends(get_db)):
    try:
        return crud.update_status(db, leave_id, "Rejected")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
