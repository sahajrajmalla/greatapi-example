from greatapi.db.admin.user import User
from greatapi.db.database import Base

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey(User.id))

    user = relationship(User)
