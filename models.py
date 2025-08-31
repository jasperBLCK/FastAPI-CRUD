from sqlalchemy import Column, Integer, String
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    password = Column(String)

    def __repr__(self):
        return f"<User id={self.id} name={self.name} age={self.age} password={self.password}>"
    
class Content(Base):
    __tablename__ = "contents"
    
    id = Column(Integer, primary_key=True, index=True)
    author = Column(String, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    
    
    def __repr__(self):
        return f"<User id={self.id} author={self.author} title={self.title}>"
