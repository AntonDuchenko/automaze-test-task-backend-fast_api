from database import Base
from sqlalchemy import Boolean, String, Integer, Column, CheckConstraint

class TodosTable(Base):
  __tablename__ = "fast-api-todos"
  
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String, index=True)
  priority = Column(Integer, index=True)
  completed = Column(Boolean, default=False)
