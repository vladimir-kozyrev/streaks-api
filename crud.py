from sqlalchemy.orm import Session
import schemas
from models.user import UserModel
from models.habit import HabitModel
from schemas.user import UserCreateSchema
from schemas.habit import HabitCreateSchema

def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(UserModel).filter(UserModel.name == name).first()

def get_users(db: Session):
    return db.query(UserModel).all()

def create_user(db: Session, user: UserCreateSchema):
    db_user = UserModel(name=user.name, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, name: str):
    db_user = get_user_by_name(db, name)
    db.delete(db_user)
    db.commit()
    return db_user

def get_habits(db: Session, habit_id: int):
    return db.query(HabitModel).filter(HabitModel.id == habit_id).all()

def create_habit(db: Session, habit: HabitCreateSchema, user_id: int):
    db_habit = HabitModel(**habit.dict(), user_id=user_id)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit
