from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'




#models.session.commit()
#models.session.new

    id = Column(Integer, primary_key=False)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>'

if __name__ == '__main__':
    Base.metadata.create_all(engine)


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