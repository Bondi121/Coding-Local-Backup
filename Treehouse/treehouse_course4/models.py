from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///seve.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()



class User(Base):
    __tablename__ = 'seve'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>'


if __name__ == '__main__':
    Base.metadata.create_all(engine)


#py -m pip install --user virtualenv
#python -m venv envSession = sessionmaker(bind=engine)
session = Session()
#.\env\Scripts\activate
#pip freeze > requirements.txt


#sqlite3.exe seve.db
#cd C:\sqlite
#sqlite3.exe C:\Users\gabri\OneDrive\Coding\Treehouse\treehouse_course4\seve.db
#C:\Users\gabri\OneDrive\Coding\Treehouse\treehouse_course4
#.tables



#in python shell
#import models
#jethro = models.User(name='Jethr', fullname='Jethro Amendola', nickname='Bubba')
#models.session.add(jethro)
#models.session.new
#will show new entry
#update entry:

#jethro.name = 'Jethro'
#models.session.new
#should show updated entry
#jethro.nickname = 'Jetty'  
#models.session.new
#empty set
#models.session.dirty
#updated set

#models.session.commit()
#exit()

#sqlite3 users.exe

#.tables
#SELECT * FROM users;
#should display a list
#.exit

#import models
#jethro = models.session.query(models.User).filter(models.User.name == 'Jethro').one()
#jethrotest = models.session.query(models.User).filter(models.User.name == 'Jethr').one()
#jethro

#jethro.nickname = 'Bubba'
#models.session.dirty

#aang = models.User(name='Aang', fullname='Avatar Aang', nickname='Aangie')
#models.session.add(aang)
#models.session.new  

#models.session.rollback()
#models.session.dirty

#models.session.new

#models.session.add(aang)
#up arrow

#models.session.new

#models.session.commit()
#models.session.delete(aang)
#models.session.commit()

#models.session.query(models.User).filter(models.User.name=='Aang').one()
#models.session.query(models.User).filter(models.User.name=='Aang').count()

#error message

#import models
#models.session.query(models.User)
#for user in models.session.query(models.User):
    #print(user)
    #enter
#for user in models.session.query(models.User.name):
    #print(user)
    #enter

#for user in models.session.query(models.User.name):
    #print(user.name)
    #enter

#for user in models.session.query(models.User.name).order_by(models.User.name):
    #print(user.name)

#for user in models.session.query(models.User.name).order_by(models.User.name.desc()):
    #print(user.name)

#for user in models.session.query(models.User.name).order_by(models.User.name)[:2]:
    #print(user.name)

#for user in models.session.query(models.User.name).order_by(models.User.name)[2:4]:
    #print(user.name)

#models.session.query(models.User).all()
#models.session.query(models.User).order_by(models.User.name).first()
#models.session.query(models.User).filter_by(name='Jethro')
#models.session.query(models.User).filter(models.User.name=='jethro')
#for user in models.session.query(models.User).filter(models.User.name=='Jethro'):
    #print(user)

#me = models.User(name='Megan', fullname='Megan Amendola', nickname='Megatron')
#models.session.add(me)
#models.session.commit()
#for user in models.session.query(models.User).filter(models.User.name=='Megan'):
    #print(user)
#for user in models.session.query(models.User).filter(models.User.name=='Megan').filter(models.User.nickname=='Megatron'):
    #print(user)

#cat = models.User(name='Joni', fullname='Joni the Cat', nickname='Key Grip')
#models.session.add(cat)
#for user in models.session.query(models.User):
    #print(user)
#cat.nickname = 'Producer'
##for user in models.session.query(models.User):
    #print(user)

#models.session.commit()



