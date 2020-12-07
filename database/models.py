from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, ARRAY, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("postgresql://postgres:sasha2705@localhost/articles", echo = True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column('id',Integer,primary_key=True)
    username = Column('username',String)
    firstname = Column('firstname',String)
    lastname = Column('lastname',String)
    email = Column('email',String,unique=True)
    password = Column('password',String)
    ustatus = Column('ustatus',String)

class Articles(Base):
    __tablename__ = 'articles'

    id = Column('id',Integer,primary_key=True)
    title = Column('title',String)
    text = Column('text',String)
    korystuvach = Column('korystuvach',String)
    status = Column('status',String)
    comlete = Column('complete',BOOLEAN)