from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db = create_engine("sqlite:///banco.db")

session = sessionmaker(bind=db)







