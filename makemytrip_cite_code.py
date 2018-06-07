import string
from threading import Thread
import requests
import csv
import time

city_code_list = []
def job(city_code,i):
    url = "https://www.makemytrip.com/pwa/framework/hotel/listing/scroll"
    querystring = {
        "checkin": "07062018",
        "checkout": "07072018",
        "city": city_code,
        "country": "IN",
        "limit": "2500000",
        "roomCount": "1"
    }

    headers = {
        'cache-control': "no-cache",
        'postman-token': "49c30640-ecf8-98ee-df40-3253c4091145"
    }
    try :
        response = requests.request("GET", url, headers=headers, params=querystring)
        chk = len(response.json().get("data"))
        if(chk > 0):
            csv_writer.writerow([city_code])
            print ("#"*20)
            print ("S.No.",i)
            print ("City Code :",city_code)
            print ("data count",chk)
            t.isAlive = False
        else:
            pass
    except :
        pass




def driver():
    buffer = string.ascii_uppercase[:26]
    list1 = list()
    for item in buffer:
        list1.append(item)

    list2, list3 = list1, list1
    i=0
    for char1 in list1:
        for char2 in list2:
            for char3 in list3:
                i=i+1
                city_code = char1 + char2 + char3
                t = Thread(target=job, args=[city_code ,i])
                t.daemon = True
                time.sleep(.1)
                t.start()


if __name__ == "__main__":
    with open('make_my_trip_city_code.csv', 'a') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        driver()