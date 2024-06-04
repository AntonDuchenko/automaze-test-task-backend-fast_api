from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine(
  'postgresql://todos_fphh_user:oHpWd86loDIc94NdwYdYtSWjLz01dK1c@dpg-cpe4of5ds78s73eqbuhg-a.frankfurt-postgres.render.com/todos_fphh'
)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

class Base(DeclarativeBase):
  pass

