from models import Session, Articles, User, Uarticles

session1 = Session()

user1 = User(id=1,username='kamysh',firstname='bogdan',lastname='lopez',email='ilove@gmail.com',password='12345',ustatus='moderator')
user2 = User(id=2,username='kamyshs',firstname='bogdans',lastname='lopezs',email='iloves@gmail.com',password='12345s',ustatus='user')

article1 = Articles(aid=1,title='end of dthe worlda',text='aaaaaaaaaaaaaaaDaaaaaaaa,panic',date='10/07/20,11.00',status='admitted')

redainfo1 = Uarticles(art_id=1, us_id=2, mod_id=1,  ed_text='aoaoaooaaoao,p', ed_date='10/07/2020,15.00')

session1.add(user1)
session1.commit()
session1.add(user2)
session1.commit()
session1.add(article1)
session1.commit()
session1.add(redainfo1)
session1.commit()



session1.close()

# psql -h localhost -d articles -U postgres -p 5432 -a -q -f create_tables.sql
# python add_models.py 
# alembic revision --autogenerate
# alembic upgrade head