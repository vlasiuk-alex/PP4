from sqlalchemy import or_

from models import Session, Users, Articles, Uarticles



def create_entry(model_class, *, commit=True, **kwargs):
    session = Session()
    entry = model_class(**kwargs)
    session.add(entry)
    if commit:
        session.commit()
    return entry


def get_entry_by_id(model_class, id):
    session = Session()
    return session.query(model_class).filter_by(id=id).one()
def get_entry_by_aid(model_class, aid):
    session = Session()
    return session.query(model_class).filter_by(aid=aid).one()

def update_entry(entry, *, commit=True, **kwargs):
    session = Session()
    for key, value in kwargs.items():
        setattr(entry, key, value)
    if commit:
        session.commit()
    return entry
    
def delete_entry(model_class, id, *, commit=True):
    session = Session()
    session.query(model_class).filter_by(id=id).delete()
    if commit:
        session.commit()
def delete_entrya(model_class, aid, *, commit=True):
    session = Session()
    session.query(model_class).filter_by(aid=aid).delete()
    if commit:
        session.commit()

def list_users(email=None, first_name=None, last_name=None):
    session = Session()
    filters = []
    if email:
        filters.append(user.email.like(email))
    if firstname:
        filters.append(user.email.like(first_name))
    if lastname:
        filters.append(Users.email.like(last_name))
    return session.query(user).filter(*filters).all()

def list_articles():
    session = Session()
    return session.query(articles).all()













