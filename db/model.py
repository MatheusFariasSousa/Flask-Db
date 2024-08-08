from db.base import Base
from sqlalchemy.orm import mapped_column,Mapped,registry


table = registry()


@table.mapped_as_dataclass
class User(Base):
    __tablename__="users"

    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str] = mapped_column(nullable=False)
    cpf:Mapped[str] = mapped_column(nullable=False,unique=True)



    


