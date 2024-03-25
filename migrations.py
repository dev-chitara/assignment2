from db_setup import engine, Base
from models import students

Base.metadata.create_all(bind=engine)