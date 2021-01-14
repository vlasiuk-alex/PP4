from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, ARRAY, BOOLEAN
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from werkzeug.security import generate_password_hash

engine = create_engine("postgresql://postgres:sasha2705@localhost/articles", echo = True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Users(Base):
    __tablename__ = "users"

    id = Column('id',Integer,primary_key=True)
    username = Column('username',String)
    firstname = Column('firstname',String)
    lastname = Column('lastname',String)
    email = Column('email',String,)
    password = Column('password',String)
    ustatus = Column('ustatus',String)
    def __init__(self, username, firstname,lastname, email,password, ustatus ):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = generate_password_hash(password)
        self.ustatus = ustatus

class Articles(Base):
    __tablename__ = 'articles'

    aid = Column('id',Integer,primary_key=True)
    title = Column('title',String)
    text = Column('text',String)
    date = Column('date',String)
    status = Column('status',String)

class Uarticles(Base):
    __tablename__ = "uarticles"

    art_id = Column('art_id',Integer,primary_key=True)
    us_id = Column('us_id',Integer)
    mod_id = Column('mod_id',Integer)
    ed_text = Column('ed_text',String)
    ed_date = Column('ed_date',String)