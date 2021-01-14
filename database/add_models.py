from models import Session, Articles, User

session1 = Session()

user1 = User(id=1,username='kamysh',firstname='bogdan',lastname='lopez',email='ilove@gmail.com',password='12345',ustatus='moderator')
article1 = Articles(id=1,title='end of the world',text='aaaaaaaaaaaaaaaaaaaaaaa,panic',korystuvach='kamysh',status='admitted',comlete=True)

session1.add(user1)
session1.add(article1)

session1.commit()

session1.close()

# psql -h localhost -d musiclist -U postgres -p 5432 -a -q -f create_tables.sql
# python add_models.py - чекнути пгадмін
# alembic revision --autogenerate
# alembic upgrate head