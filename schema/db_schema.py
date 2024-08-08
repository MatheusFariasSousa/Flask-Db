from pydantic import BaseModel,field_validator
import re

class Db_schema(BaseModel):
    name:str
    cpf:str


    @field_validator("cpf")
    def cpf_validade(cls,cpf):
        if not re.match(cpf,"^[0-9]+8$"):
            raise Exception
        return cpf



