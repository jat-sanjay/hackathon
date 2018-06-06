from bs4 import BeautifulSoup
import time
from threading import Thread
import requests
from sqlalchemy import Column, DateTime, String, Integer,func,create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class CustomBase(Base):
    __abstract__ = True
    created_at = Column(DateTime, default=func.now())

# ------------------- Movies model- stores Movies info -----------------------------------
class Movies(CustomBase):
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False,index=True)
    name = Column(String(255), default=None)
    size = Column(String(255), default=None)
    url = Column(String(255), default=None ,primary_key=True,nullable=False ,unique=True,index=True)
    extension = Column(String(255), default=None)
    format = Column(String(255), default=None)
    owner = Column(String(255), default=None)
    __tablename__ = 'Movies'

    def __init__(self, name=None, size=None, url=None, extension=None, format=None, owner=None):
        self.name = name
        self.size = size
        self.url = url
        self.extension = extension
        self.format = format
        self.owner = owner

    def __repr__(self):
        return self.phone

    # def is_authenticated(self):   #can be used if required
    #    return True

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

def getSession():
    session = sessionmaker()
    session.configure(bind=engine)
    session = session()
    return session

def job(i):
    try:
        url = "http://drive.pahe.in/file/" + str(i)
        """ Response from url """
        resp = requests.get(url)
        print("#### Visiting:", url)
        """ parse response to lxml """
        soup = BeautifulSoup(resp.content, 'lxml')
        data = soup.find('tbody')
        each_link_data = dict()
        for tr in data.find_all('tr'):
            td = tr.find_all('td')
            local_data = {
                td[0].text: td[1].text.replace("\t", "").replace("\n", "")
            }
            each_link_data.update(local_data)
        print("**** Found:", each_link_data)
        print("-" * 20)
        name = each_link_data.get('File Name')
        size = each_link_data.get('File Size')
        format = each_link_data.get('File Type')
        owner = each_link_data.get('File Owner')
        extension = each_link_data.get('File Extension')
        # url = url
        movie = Movies(name,size,url,extension,format,owner)
        session = getSession()
        session.add(movie)
        session.commit()
        t.isAlive = False
    except Exception as e:
        pass


if __name__ == "__main__":
    engine = create_engine('mysql://root:@localhost/pahe_db?charset=utf8', pool_size=200)
    Base.metadata.create_all(engine)
    for i in range(1, 91000):
        t = Thread(target=job, args=[i])
        t.daemon = True
        time.sleep(.1)
        t.start()



