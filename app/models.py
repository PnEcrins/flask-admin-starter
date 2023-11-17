from app.env import db


from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Foo(db.Model):
    __tablename__ = "foo"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


