from src.core.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(String)
    date = Column(DateTime)
    user = Column(Integer, ForeignKey('users.id'))
    user_id = relationship("User")