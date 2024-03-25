from uuid import UUID
from typing import List

from models.students import Student
from schemas.students import CreateStudentSchema, UpdateStudentSchema, GetStudentSchema
from db_setup import get_db

from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session



router = APIRouter(tags=["Student API"])



@router.get("/students", status_code=status.HTTP_200_OK, response_model=List[GetStudentSchema])
async def fetch_students(db: Session=Depends(get_db)):
    student_objects = db.query(Student).all()
    return student_objects


@router.post("/students", status_code=status.HTTP_201_CREATED, response_model=GetStudentSchema)
async def create_students(student_data: CreateStudentSchema, db: Session=Depends(get_db)):
    student_object = Student(**student_data.model_dump())
    db.add(student_object)
    db.commit()
    db.refresh(student_object)
    return student_object


@router.get("/students/{student_id}", status_code=status.HTTP_200_OK, response_model=GetStudentSchema)
async def get_student(student_id: UUID, db: Session=Depends(get_db)):
    student_object = db.query(Student).filter(Student.id == student_id).first()

    if student_object is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail={"message": "Student does not found!"}
        )
    
    return student_object


@router.patch("/students/{student_id}", status_code=status.HTTP_200_OK, response_class=GetStudentSchema)
async def update_students(student_id: UUID, student_data: UpdateStudentSchema, db: Session=Depends(get_db)):
    update_student_data = student_data.model_dump(exclude_none=True)

    student_query = db.query(Student).filter(Student.id == student_id)
    student_object = student_query.first()

    if student_object is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "Student does not found!"}
        )
    
    student_query.update(update_student_data)
    db.commit()
    db.refresh(student_object)
    return student_object


@router.delete("/students/{student_id}",status_code=status.HTTP_200_OK)
async def delete_student(student_id: UUID, db: Session=Depends(get_db)):
    student_object = db.query(Student).filter(Student.id == student_id).first()

    if student_object is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "Student does not found!"}
        )
    
    db.delete(student_object)
    db.commit()
    return {"Deleted": True}