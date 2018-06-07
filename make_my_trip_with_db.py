import time
from threading import Thread
import requests
from sqlalchemy import Column, DateTime, String, Integer,func,create_engine,Text,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
import csv

BASEURL = "https://dtr-hoteldom.makemytrip.com/mmthtl/site/getMoreReviewsNew"


Base = declarative_base()

class CustomBase(Base):
    __abstract__ = True
    created_at = Column(DateTime, default=func.now())

# ------------------- Movies model- stores Movies info -----------------------------------
# travellerName,travelType,title,userRating,checkinDate,checkoutDate,reviewDate,description,images,videos,ratingText



class Person(CustomBase):
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False,index=True)
    hotel_id = Column(String(255), default=None)
    name = Column(String(255), default=None)
    hotel_name = Column(String(255), default=None)
    hotel_address = Column(Text, default=None)
    type = Column(String(255), default=None)
    title = Column(String(255), default=None)
    rating = Column(String(255), default=None)
    check_in_date = Column(String(255), default=None)
    check_out_date = Column(String(255), default=None)
    review_date = Column(String(255), default=None)
    description = Column(Text, default=None)
    review_text = Column(Text,default=None)

    __tablename__ = 'Person'

    def __init__(self, hotel_id=None,name=None,hotel_name=None,type=None,hotel_address=None, title=None, rating=None, check_in_date=None, check_out_date=None, review_date=None,description=None,review_text=None):
        self.hotel_id=hotel_id
        self.name = name
        self.hotel_name=hotel_name
        self.hotel_address = hotel_address
        self.type=type
        self.title = title
        self.rating = rating
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.review_date = review_date
        self.description=description
        self.review_text=review_text

    def __repr__(self):
        return self.name

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



def get_all_reviews(hotel_id, num_reviews=99999999, country="IN", type="MMT", sort="D", start="0"):
    """
    :param hotel_id: Id of the hotel to get reviews for.
    :param num_reviews: Number of reviews. Defaults to all.
    :param country: Country of the hotel. Defaults to India
    :param type: Type of reviews. Defaults to MMT.
    :param sort: To sort in Ascending or Descending order chronologically.
    :param start: Use this for pagination of reviews to get reviews in chunks.
    :return: list of all reviews for the given hotel id.
    """

    payload = {
        "hotelId": hotel_id,
        "numReviews": num_reviews,
        "country": country,
        "type": type,
        "sort": sort,
        "start": start
    }
    try:
        response = requests.get(BASEURL, params=payload)
        all_review = response.json().get("review_list")
        return all_review
    except :
       pass
    return

def hotel_details_by_city_code(cityCode):
    url = "https://www.makemytrip.com/pwa/framework/hotel/listing/scroll"
    querystring = {
        "checkin": "07062018",
        "checkout": "07072018",
        "city": cityCode,
        "country": "IN",
        "limit": "2500000",
        "roomCount": "1"
    }

    headers = {
        'cache-control': "no-cache",
        'postman-token': "49c30640-ecf8-98ee-df40-3253c4091145"
    }
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json().get("data")
        for item in data:
            hotel_id = item.get("data").get("hotel_id")
            hote_name = item.get("data").get("hotel_name")
            hotel_address1 = item.get("data").get("hotel_address").get("line1")
            hotel_address2 = item.get("data").get("hotel_address").get("line2")
            if hotel_address1 and hotel_address2:
                hotel_address = hotel_address1 + hotel_address2
            elif hotel_address1:
                hotel_address = hotel_address1
            elif hotel_address2:
                hotel_address = hotel_address2
            else:
                hotel_address = "No address of this hotel"
            return hotel_id, hote_name, hotel_address
    except:
        pass


def get_all_review_of_given_hotel_id(hotel_id,hotel_name,hotel_address):
    try:
        all_review = get_all_reviews(hotel_id)
        for item in all_review:
            name = item.get("travellerName")
            type = item.get("travelType")
            title = item.get("title")
            rating = item.get("userRating")
            checkin_date = item.get("checkinDate")
            checkout_date = item.get("checkoutDate")
            review_date = item.get("reviewDate")
            description = item.get("description")
            rating_text = item.get("ratingText")
            person = Person(hotel_id, name, hotel_name, type, hotel_address, title, rating, checkin_date, checkout_date,
                            review_date, description, rating_text)
            session = getSession()
            session.add(person)
            session.commit()
            print ("#" * 40)
            print ("#Visiting Hotel : ", hotel_name)
            print ("#Hotel Rating Text :", rating_text)

    except:
        pass


def driver():
    with open("make_my_trip_city_code.csv", "r") as f:
        try:
            reader = csv.reader(f, delimiter="\t")
            for city_code in reader:
                cityCode = city_code[0]
                hotel_id,hotel_name,hotel_address =hotel_details_by_city_code(cityCode)
                t = Thread(target=get_all_review_of_given_hotel_id, args=[hotel_id,hotel_name,hotel_address])
                t.daemon = True
                time.sleep(.3)
                t.start()
        except:
            pass

if __name__ == "__main__":
    engine = create_engine('mysql://root:@localhost/makemytrip_db?charset=utf8', pool_size=200)
    Base.metadata.create_all(engine)
    driver()

