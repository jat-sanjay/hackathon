from bs4 import BeautifulSoup
import csv
import time
from threading import Thread
import requests

def job(i):
    try:
        url = "http://drive.pahe.in/file/"+str(i)
        resp = requests.get(url)
        print("#### Visiting:", url)
        soup = BeautifulSoup(resp.content,'lxml')
        data  = soup.find('tbody')
        each_link_data  = dict()
        for tr in data.find_all('tr'):
            td = tr.find_all('td')
            local_data = {
                td[0].text : td[1].text.replace("\t","").replace("\n","")
            }
            each_link_data.update(local_data)
        print("**** Found:", each_link_data)
        t.isAlive=False
        list = []
        print("-"*20)
        for key , value in each_link_data.items():
            list.append(value)
        list.append(url)
        csv_writer.writerow(list)
    except Exception as e:
        pass

with open('pahe_data1.csv', 'a') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(79997,90000):
        t = Thread(target=job, args=[i])
        t.daemon = True
        time.sleep(.1)
        t.start()


