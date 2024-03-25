from uuid import UUID
from datetime import datetime
from pydantic import BaseModel


class BaseStudentSchema(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: datetime
    grade: int
    phone: str
    email: str


class CreateStudentSchema(BaseStudentSchema):
    pass


class UpdateStudentSchema(BaseStudentSchema):
    first_name: str | None=None
    last_name: str | None=None
    date_of_birth: datetime | None=None
    grade: int | None=None
    phone: str | None=None
    email: str | None=None


class GetStudentSchema(BaseStudentSchema):
    id: UUID

    class Config:
        from_attributes = True