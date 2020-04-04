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

@app.get("/v1/users", response_model=List[UserSchema])
def get_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users


@app.post("/v1/users", response_model=UserSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="A user with that email already exists.")
    return crud.create_user(db=db, user=user)


@app.put("/v1/users", response_model=UserSchema)
def update_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        return crud.update_user(db=db, existing_user=db_user, updated_user=user)
    return crud.create_user(db=db, user=user)


@app.delete("/v1/user/{email}", response_model=UserSchema)
def delete_user(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=400, detail="User does not exist.")
    return crud.delete_user(db, email)
