from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from backend.dto import UserCreate

user_router = APIRouter()


def get_db():
    db = session_factory() #создаем ноую сессию
    try:
        yield db
    finally:
        db.close()

@user_router.post("/user/{user_id}/create")
def add(user_create: UserCreate, db: Session = Depends(get_db)):
    login =
