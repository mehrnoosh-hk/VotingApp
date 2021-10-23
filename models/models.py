from .database import Base
from sqlalchemy import Column, Integer, Text, ARRAY


# TODO: Create pool class
class Poll(Base):
    __tablename__ = "polls"
    id = Column(Integer, primary_key=True)
    question = Column(Text)
    description = Column(Text)
    options = Column(ARRAY(Text))
