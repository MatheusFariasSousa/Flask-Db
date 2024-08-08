from connection import session
from sqlalchemy.orm import Session

def conection():
    try:
        session =Session()
        yield session
    finally:
        session.close()
 