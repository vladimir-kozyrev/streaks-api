from sqlalchemy.orm import Session
import schemas
from models.user import UserModel
from models.habit import HabitModel
from schemas.user import UserCreateSchema, UserSchema
from schemas.habit import HabitCreateSchema

def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(UserModel).filter(UserModel.email == email).first()

def get_users(db: Session):
    return db.query(UserModel).all()

def update_user(db: Session, existing_user: UserSchema, updated_user: UserCreateSchema):
    existing_user.name = updated_user.name
    existing_user.password = updated_user.password
    db.add(existing_user)
    db.commit()
    db.refresh(existing_user)
    return existing_user

def create_user(db: Session, user: UserCreateSchema):
    db_user = UserModel(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, email: str):
    db_user = get_user_by_email(db, email)
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
