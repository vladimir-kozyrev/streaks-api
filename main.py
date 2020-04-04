from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from schemas.user import UserSchema, UserCreateSchema
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post("/users", response_model=UserSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="A user with that name already exists.")
    return crud.create_user(db=db, user=user)

@app.get("/users", response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@app.delete("/user/{name}", response_model=UserSchema)
def delete_user(name: str, db: Session = Depends(get_db)):
    return crud.delete_user(db, name)
