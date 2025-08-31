from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    name: str
    age: int
    password: str

class UserRead(BaseModel):
    id: int
    name: str
    age: int


class PostCreate(BaseModel):
    author: str = Field(min_length=1, max_length=10)
    title: str = Field(max_length=20)
    content: str = Field(max_length=300)
    
class PostRead(BaseModel):
    id: int
    author: str 
    title: str
    content: str
    


    class Config:
        from_attributes = True  


class PostUpdate(BaseModel):
    author: Optional[str] = Field(None, min_length=1, max_length=10)
    title: Optional[str] = Field(None, max_length=20)
    content: Optional[str] = Field(None, max_length=300)