from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import SessionLocal, engine, Base
from models import Content, User
from schemas import UserCreate, UserRead, PostCreate, PostRead, PostUpdate

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- USERS ----------------
@app.post("/users", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, age=user.age, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users", response_model=list[UserRead])
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()


# модель для удаления пользователя по имени и паролю
class UserLogin(BaseModel):
    name: str
    password: str

@app.delete('/users')
def user_delete(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.name == user.name).first()
    if not db_user:
        raise HTTPException(404, "User not found")
    
    if db_user.password != user.password:
        raise HTTPException(401, "Invalid password")
    
    db.delete(db_user)
    db.commit()
    return {"message": f"User {user.name} deleted successfully"}


# ---------------- CONTENT ----------------
@app.post("/contents", response_model=PostRead)
def create_content(content: PostCreate, db: Session = Depends(get_db)):
    db_post = Content(author=content.author, title=content.title, content=content.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


@app.get("/contents", response_model=list[PostRead])
def read_post(db: Session = Depends(get_db)):
    return db.query(Content).all()


@app.put("/contents/{content_id}", response_model=PostRead)
def update_content(content_id: int, updated_content: PostUpdate, db: Session = Depends(get_db)):
    db_post = db.query(Content).filter(Content.id == content_id).first()
    if not db_post:
        raise HTTPException(status_code=404, detail="Content not found")

    if updated_content.author is not None:
        db_post.author = updated_content.author
    if updated_content.title is not None:
        db_post.title = updated_content.title
    if updated_content.content is not None:
        db_post.content = updated_content.content

    db.commit()
    db.refresh(db_post)
    return db_post


@app.delete('/contents/{content_id}')
def delete_content(content_id: int, db: Session = Depends(get_db)):
    db_post = db.query(Content).filter(Content.id == content_id).first()
    if not db_post:
        raise HTTPException(404, 'ID Not found')
    
    db.delete(db_post)
    db.commit()
    return {"message": f"Post with id={content_id} deleted successfully"}
