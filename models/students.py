import uuid
from sqlalchemy import Column, UUID, Integer, String, Date
from db_setup import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String(100))
    last_name = Column(String(100))
    date_of_birth = Column(Date)
    grade = Column(Integer)
    phone = Column(String(100))
    email = Column(String(100))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"