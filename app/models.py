from sqlalchemy import DateTime, String, Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime, timezone

class Posts(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    content = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="posts")

    published_date = Column(DateTime, default=datetime.now(timezone.utc))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))

    posts = relationship("Posts", back_populates="owner")

