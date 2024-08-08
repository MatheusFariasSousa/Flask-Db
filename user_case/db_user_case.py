from sqlalchemy.orm import Session
from schema.db_schema import Db_schema
from db.model import User


class UserCase:
    def __init__(self,db_session:Session):
        self.db_session = db_session


    def post_method(self,user:Db_schema):
        person = User(name = user.name,cpf = user.cpf)
        cpf_validate = self.db_session.query(User).where(User.cpf == user.cpf).first()
        if cpf_validate:
            return "This cpf have been use"
        self.db_session.add(person)
        self.db_session.commit()
            
        