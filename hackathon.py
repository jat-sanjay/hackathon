import requests
import json
import time
from bs4 import BeautifulSoup
from flask import jsonify,request,render_template,url_for
from splinter import Browser
import flask
import jinja2
from flask_cors import CORS

app=flask.Flask(__name__);
CORS(app)
def remPunct(my_str):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in my_str:
        if char not in punctuations:
            no_punct = no_punct + char

        if char in punctuations:
            no_punct = no_punct + " "

    return no_punct






mydict = {
    "64": "ADARSH NAGAR",
    "99": "AIIMS",
    "67": "AKSHARDHAM",
    "81": "ANAND VIHAR",
    "108": "ARJANGARH",
    "82": "ASHOK PARK MAIN",
    "63": "AZADPUR",
    "130": "BADARPUR",
    "146": "BADKAL MOR",
    "28": "BARAKHAMBA",
    "149": "BATA CHOWK",
    "74": "BOTANICAL GARDEN",
    "56": "CENTRAL SECRETARIAT",
    "34": "CHANDNI CHOWK",
    "33": "CHAWRI BAZAR",
    "105": "CHHATTARPUR",
    "40": "CIVIL LINES",
    "139": "DELHI AERO CITY",
    "154": "DELHI GATE",
    "138": "DHAULA KUAN",
    "60": "DILSHAD GARDEN",
    "7": "DWARKA",
    "8": "DWARKA MOR",
    "2": "DWARKA SEC 10",
    "3": "DWARKA SEC 11",
    "4": "DWARKA SEC 12",
    "5": "DWARKA SEC 13",
    "6": "DWARKA SEC 14",
    "115": "DWARKA SECTOR 21",
    "114": "DWARKA SEC 8",
    "1": "DWARKA SEC 9",
    "150": "ESCORTS MUJESAR",
    "61": "G.T.B. NAGAR",
    "107": "GHITORNI",
    "75": "GOLF COURSE",
    "124": "GOVIND PURI",
    "100": "GREEN PARK",
    "109": "INDIGO GURU DRONACHARYA",
    "151": "HAIDERPUR BADLI MOR",
    "101": "HAUZ KHAS",
    "113": "SHALIMAR HUDA CITY CENTER",
    "140": "I.G.I. AIRPORT",
    "112": "IFFCO CHOWK",
    "98": "INA",
    "46": "INDER LOK",
    "31": "INDRAPRASTHA",
    "141": "ITO",
    "65": "JAHANGIRPURI",
    "155": "JAMA MASJID",
    "161": "JAMIA MILIA ISLAMIYA",
    "13": "JANAK PURI EAST",
    "12": "JANAKPURI WEST",
    "118": "JANGPURA",
    "136": "JANPATH",
    "126": "JASOLA APOLLO",
    "159": "JASOLA VIHAR",
    "25": "JHANDEWALAN",
    "59": "JHIL MIL",
    "117": "JLN STADIUM",
    "97": "JORBAGH",
    "121": "KAILASH COLONY",
    "158": "KALINDI KUNJ",
    "123": "KALKAJI MANDIR",
    "47": "KANHAIYA NAGAR",
    "80": "KARKAR DUMA",
    "24": "KAROL BAGH",
    "35": "KASHMERE GATE",
    "131": "KAUSHAMBI",
    "48": "KESHAV PURAM",
    "116": "KHAN MARKET",
    "20": "KIRTI NAGAR",
    "50": "KOHAT ENCLAVE",
    "119": "LAJPAT NAGAR",
    "156": "LAL QUILA",
    "77": "LAXMI NAGAR",
    "96": "LOK KALYAN MARG",
    "111": "SYSKA LED MG ROAD",
    "85": "MADI PUR",
    "102": "MALVIYA NAGAR",
    "29": "MANDI HOUSE",
    "58": "MANSAROVAR PARK",
    "68": "MAYUR VIHAR-I",
    "69": "MAYUR VIHAR-I EXT",
    "144": "MEWALA MAHARAJPUR",
    "62": "MODEL TOWN",
    "128": "MOHAN ESTATE",
    "120": "MOOLCHAND",
    "19": "MOTI NAGAR",
    "94": "MUNDKA",
    "91": "NANGLOI",
    "92": "NANGLOI RLY. STATION",
    "9": "NAWADA",
    "148": "NEELAM CHOWK AJRONDA",
    "122": "NEHRU PLACE",
    "49": "NETAJI SUBHASH PLACE",
    "70": "NEW ASHOK NAGAR",
    "32": "NEW DELHI",
    "143": "NHPC CHOWK",
    "78": "NIRMAN VIHAR",
    "76": "WAVE CITY CENTRE NOIDA",
    "71": "NOIDA SEC 15",
    "72": "NOIDA SEC 16",
    "73": "WAVE SECTOR 18 NOIDA",
    "163": "NSIC OKHLA",
    "125": "OKHLA",
    "157": "OKHLA BIRD SANCTUARY",
    "160": "OKHLA VIHAR",
    "147": "OLD FARIDABAD",
    "86": "PASCHIM VIHAR (EAST)",
    "87": "PASCHIM VIHAR (WEST)",
    "55": "PATEL CHOWK",
    "22": "PATEL NAGAR",
    "88": "PEERA GARHI",
    "51": "PITAM PURA",
    "30": "PRAGATI MAIDAN",
    "45": "PRATAP NAGAR",
    "79": "PREET VIHAR",
    "44": "PUL BANGASH",
    "83": "PUNJABI BAGH",
    "104": "QUTAB MINAR",
    "93": "RAJDHANI PARK",
    "23": "RAJENDRA PLACE",
    "27": "RAJIV CHOWK",
    "17": "RAJOURI GARDEN",
    "18": "RAMESH NAGAR",
    "54": "RITHALA",
    "26": "RK ASHRAM MARG",
    "52": "ROHINI EAST",
    "152": "ROHINI SECTOR 18,19",
    "53": "ROHINI WEST",
    "103": "SAKET",
    "153": "SAMAYPUR BADLI",
    "142": "SARAI",
    "127": "SARITA VIHAR",
    "133": "SATGURU RAM SINGH MARG",
    "145": "SECTOR-28",
    "37": "SEELAMPUR",
    "21": "SHADIPUR",
    "39": "SHAHDARA",
    "57": "SHASTRI NAGAR",
    "36": "SHASTRI PARK",
    "84": "SHIVAJI PARK",
    "137": "ONGC SHIVAJI STADIUM",
    "110": "SIKANDARPUR",
    "15": "SUBHASH NAGAR",
    "162": "SUKHDEV VIHAR",
    "106": "SULTANPUR",
    "90": "SURAJMAL STADIUM",
    "16": "TAGORE GARDEN",
    "14": "TILAK NAGAR",
    "43": "TIS HAZARI",
    "129": "TUGHLAKABAD",
    "95": "UDYOG BHAWAN",
    "89": "UDYOG NAGAR",
    "11": "UTTAM NAGAR EAST",
    "10": "UTTAM NAGAR WEST",
    "132": "DAINIK JAGRAN VAISHALI",
    "41": "VIDHAN SABHA",
    "42": "VISHWAVIDYALAYA",
    "38": "WELCOME",
    "66": "YAMUNA BANK"
}

def getMetroRates(src, dest):
    executable_path = {'executable_path':'chromedriver'}
    browser = Browser('chrome', **executable_path)
    with browser:
        # Visit URL

        url = "http://www.delhimetrorail.com/metro-fares.aspx"
        browser.visit(url)
        new_dict = {y:x for x,y in mydict.items()}

        browser.select('ctl00$MainContent$ddlFrom',new_dict[src.upper()])
        browser.select('ctl00$MainContent$ddlTo',new_dict[dest.upper()])
        button = browser.find_by_name('ctl00$MainContent$btnShowFare')



        button.click()
        fare = browser.find_by_xpath('//*[@id="aspnetForm"]/div[5]/div/div/div/div/div/div[2]/div/div[1]/div[2]')
        timing = browser.find_by_xpath('//*[@id="aspnetForm"]/div[5]/div/div/div/div/div/div[2]/ul/li[1]')
        no_of_station = browser.find_by_xpath('//*[@id="aspnetForm"]/div[5]/div/div/div/div/div/div[2]/ul/li[2]')
        distance = browser.find_by_xpath('//*[@id="aspnetForm"]/div[5]/div/div/div/div/div/div[2]/ul/li[3]')
        inter_change = browser.find_by_xpath('//*[@id="aspnetForm"]/div[5]/div/div/div/div/div/div[2]/ul/li[4]')

        metro_response={ "fare":int(fare.text),
        "time":timing.text,
        "no_of_station":no_of_station.text,
        "distance" : distance.text,
        "interchange" : int(inter_change.text[-1]),
        "type": "SUBWAY"
        }

        return metro_response


#from shuttl api to get data
"""
url_shuttl = 'https://goplus.in/web/routes/slots'
header_shuttl = {
    'accept': "application/json",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9",
    'connection': "keep-alive",
    'host': "goplus.in",
    'origin': "https://m.shuttl.com",
    'platform': "web",
    'referer': "https://m.shuttl.com/slots",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
    'userid': "31776879536f4861636b794d79467269656e64",
    'cache-control': "no-cache",
    'postman-token': "8b21a52e-c6e8-ecd1-fb7e-2b3708ac8f61"
    }

shuttl_params = {
                 "fromLat": "28.412094" ,
                 "fromLng":"77.04199700000004",
                 "toLat":"28.6329822",
                 "toLng": "77.08123150000006"
                 }


response_shuttl = requests.get(url_shuttl , headers = header_shuttl, params=shuttl_params)

print(response_shuttl.json())
"""

'''
#from dmrc website to get data

url_dmrc = 'http://www.delhimetrorail.com/metro-fares.aspx'
response_dmrc = requests.get(url_dmrc)
data_dmrc = response_dmrc.text
soup_dmrc = BeautifulSoup(data_dmrc)
print(soup_dmrc)

'''


def my_shuttl(origin_lat,origin_long,dest_lat,dest_long,from_name,to_name):
    # from shuttl api to get data
    url_shuttl = 'https://goplus.in/web/routes/slots'
    header_shuttl = {
        'accept': "application/json",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "en-US,en;q=0.9",
        'connection': "keep-alive",
        'host': "goplus.in",
        'origin': "https://m.shuttl.com",
        'platform': "web",
        'referer': "https://m.shuttl.com/slots",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36",
        'userid': "31776879536f4861636b794d79467269656e64",
        'cache-control': "no-cache",
        'postman-token': "8b21a52e-c6e8-ecd1-fb7e-2b3708ac8f61"
    }



    shuttl_params = {
            "fromLat": origin_lat,
            "fromLng": origin_long,
            "toLat": dest_lat,
            "toLng": dest_long,
            "fromName":from_name,
            "toName":to_name
    }



    response_shuttl = requests.get(url_shuttl, headers=header_shuttl, params=shuttl_params)
    data = response_shuttl.json()

    print(data)
    originLat = data["data"]["fromLoc"]["lat"]
    originLong = data["data"]["fromLoc"]["lng"]
    destLat = data["data"]["toLoc"]["lat"]
    destLong = data["data"]["toLoc"]["lng"]



    traveltime = data["data"]["slots"][0]["trip"]["journeyTime"]/(1000*60)
    traveltime_mins=int(traveltime % 60)
    totalfare = data["data"]["slots"][0]["trip"]["fare"]




    details = {
        "mode_distance":"ss",
        "org_lat":originLat,
        "org_lng":originLong,
        "end_lat":destLat,
        "end_lng":destLong,
        "mode_distance_value":"ss",
        "mode_duration":"1 hr"+str(traveltime_mins)+" mins" ,
        "mode_name" :"SHUTTL",
        "rate":totalfare
    }

    print("line 331")
    return details



#from uber api to get all data

def uber_rates(origin_lat,origin_long,dest_lat,dest_long):
    url_uber = 'https://api.uber.com/v1.2/estimates/price?'
    """params_uber = (
        ('start_latitude', '28.6202196'),
        ('start_longitude', '77.3524938'),
        ('end_latitude', '28.4129062'),
        ('end_longitude', '77.0393718'),
    )"""
    params_uber={
        'start_latitude': origin_lat,
        'start_longitude': origin_long,
        'end_latitude':dest_lat,
        'end_longitude': dest_long,
        'server_token':'PSa7EFnx59T9Vw5AdkCXElYvykfVuG3vlag4eUCd'
    }

    headers_uber = {
        'cache-control': "no-cache",
        'postman-token': "b2e2a473-83de-1ba7-ec7e-e5c8798a25b3"
    }
    response_uber = requests.get(url_uber, params=params_uber, headers=headers_uber)


    return response_uber.json()




#main program


@app.route('/')
def template():
    return render_template('/hack/shuttl_hack.html')



@app.route('/fares')
def fare_templates():
    origin = request.args.get("origin")
    end = request.args.get("end")
    mode=request.args.get("mode")


    return render_template('/hack/shuttlUI1.html',origin=origin,end=end, mode=mode)



# from google map get json data
@app.route('/get_fares',methods=['GET'])
def calculate_fare():
    origin = request.args.get("origin")
    end = request.args.get("end")
    method = request.args.get("mode")
    url_googlemap = 'https://maps.googleapis.com/maps/api/directions/json'


    params_googlemap = {"origin":origin,
                        "destination":end,
                        "mode": method,
                        "key":"AIzaSyC7ZamQtydmVTDksiP6p3lJIs4EUuRtdCo"}

    headers_googlemap = {
        'cache-control': "no-cache",
        'postman-token': "b2e2a473-83de-1ba7-ec7e-e5c8798a25b3"
    }

    response_googlemap = requests.get(url_googlemap,params=params_googlemap)


    response=response_googlemap.json()

    try :
        response["routes"][0]
    except:
        print ("No routes exist")
        trip = {
            "distance": "",
            "duration": "no routes exist",
            "steps": "",
            "total_fare": ""
        }
        return jsonify(trip)

    total_dist = response["routes"][0]["legs"][0]["distance"]["text"]
    total_time = response["routes"][0]["legs"][0]["duration"]["text"]
    total_fare = 0

    steps=[]
    startlat = response["routes"][0]["legs"][0]["start_location"]["lat"]
    startlng = response["routes"][0]["legs"][0]["start_location"]["lng"]
    endlat = response["routes"][0]["legs"][0]["end_location"]["lat"]
    endlng = response["routes"][0]["legs"][0]["end_location"]["lng"]



    travel_mode = response["routes"][0]["legs"][0]["steps"][0]["travel_mode"]
    #if travel_mode == "DRIVING":

    if method=="shuttl":

        response_shuttl = my_shuttl(startlat, startlng, endlat, endlng,origin,end)

        print (jsonify(response_shuttl))
        org_lat=response_shuttl["org_lat"]
        org_lng = response_shuttl["org_lng"]
        end_lat= response_shuttl["end_lat"]
        end_lng = response_shuttl["end_lng"]

        url_shuttl = 'http://localhost:2001/get_fares'
        """
        print ("line 447")
        params_shuttl_org = {"origin": str(startlat)+","+str(startlng),
                            "destination": str(org_lat)+","+str(org_lng),
                            "mode": "transit",
                            "key": "AIzaSyC7ZamQtydmVTDksiP6p3lJIs4EUuRtdCo"}

        print("line 451")
        response_shuttl_org = requests.get(url_shuttl, params=params_shuttl_org)
        print(response_shuttl_org)

        params_shuttl_end = {"origin": str(endlat) + "," + str(endlng),
                             "destination": str(end_lat) + "," + str(end_lng),
                             "mode": "transit",
                             "key": "AIzaSyC7ZamQtydmVTDksiP6p3lJIs4EUuRtdCo"}

        response_shuttl_end = requests.get(url_shuttl, params=params_shuttl_end)
        print(response_shuttl_end)
        print("line 461")
        for itr in response_shuttl_org["steps"]:
            steps.append(itr)

        

        for itr2 in response_shuttl_end["steps"]:
            steps.append(itr2)
            """

        steps.append(response_shuttl)
        trip = {
            "distance": total_dist,
            "duration": response_shuttl["mode_duration"],
            "steps": steps,
            "total_fare": response_shuttl["rate"]
        }

        return jsonify(trip)







    if method=="uber":
        response_uber=uber_rates(startlat,startlng,endlat,endlng)
        flagshow=0
        for itr in response_uber["prices"]:
           if  itr["display_name"] == "HIRE GO" and flagshow == 0:
                mode = {
                    "mode_distance": itr["distance"],
                    "org_lat": startlat,
                    "org_lng": startlng,
                    "end_lat": endlat,
                    "end_lng": endlng,
                    "mode_distance_value": itr["distance"],
                    "mode_duration": itr["duration"],
                    "mode_name": itr["display_name"],
                    "rate": itr["low_estimate"]
                }
                total_fare=total_fare+mode["rate"]
                steps.append(mode)
                flagshow=1

           trip = {
               "distance": total_dist,
               "duration": total_time,
               "steps": steps,
               "total_fare": total_fare
           }
        return jsonify(trip)

    print (total_dist)
    print(total_time)
    count=0
    metro=0

    for i in response["routes"][0]["legs"][0]["steps"]:
        travel_mode = i["travel_mode"]

        if travel_mode=="DRIVING":

            mode_distance= i["distance"]["text"]
            mode_duration = i["duration"]["text"]

            mode = {
                "mode_distance": i["distance"]["text"],
                "org_lat": i["start_location"]["lat"],
                "org_lng": i["start_location"]["lng"],
                "end_lat": i["end_location"]["lat"],
                "end_lng": i["end_location"]["lng"],
                "mode_distance_value": i["distance"]["value"],
                "mode_duration": i["duration"]["text"],
                "mode_name": "DRIVING",
                "rate" : (i["distance"]["value"]/28000)*72
            }




        if travel_mode=="TRANSIT":

            mode_distance= i["distance"]["text"]
            mode_duration = i["duration"]["text"]

            mode = {
                "mode_distance": i["distance"]["text"],
                "org_lat": i["start_location"]["lat"],
                "org_lng": i["start_location"]["lng"],
                "end_lat": i["end_location"]["lat"],
                "end_lng": i["end_location"]["lng"],
                "mode_distance_value": i["distance"]["value"],
                "mode_duration": i["duration"]["text"],
                "mode_detail" : i["transit_details"]["line"]["vehicle"]["type"],
                "mode_name": i["transit_details"]["line"]["vehicle"]["type"],
                "rate": 0
            }

            if mode["mode_detail"] == "BUS":
                if metro == 1:
                    mode["rate"]=mode["rate"]+getMetroRates(remPunct(src), remPunct(dest))["fare"]

                    metro = 0
                try:
                    mode["mode_name"]=i["transit_details"]["line"]["short_name"]
                    mode["rate"] = mode["rate"] + 45
                except :
                    mode["mode_name"]="Bus"
                    mode["rate"] = mode["rate"] + 45





            if mode["mode_detail"]=="SUBWAY":
                if metro==0:
                    src=i["transit_details"]["departure_stop"]["name"]
                    metro=1
                    print(src)
                dest=i["transit_details"]["arrival_stop"]["name"]
            else:
                print(mode["mode_detail"])





        if travel_mode=="WALKING":

            mode={
                "mode_distance" : i["distance"]["text"],
                "org_lat" : i["start_location"]["lat"],
                "org_lng" : i["start_location"]["lng"],
                "end_lat" : i["end_location"]["lat"],
                "end_lng" : i["end_location"]["lng"],
                "mode_distance_value" : i["distance"]["value"],
                "mode_duration" : i["duration"]["text"],
                "mode_name" : "WALKING",
                "rate": 0
            }


            if mode["mode_distance_value"] > 800:
                if metro == 1:
                    mode["rate"] =  getMetroRates(remPunct(src), remPunct(dest))["fare"]
                    metro = 0
                uber=uber_rates(mode["org_lat"],mode["org_lng"],mode["end_lat"],mode["end_lng"])
                for rates in uber["prices"]:
                    type=rates["display_name"]
                    if type == "HIRE GO" or type == "uberPOOL":
                        mode["mode_name"] = type
                        mode["rate"]=rates["low_estimate"]

        total_fare = total_fare + mode["rate"]
        steps.append(mode)
        print()

    if metro==1:
        total_fare = total_fare + getMetroRates(remPunct(src), remPunct(dest))["fare"]
        metro=0

    trip={
        "distance" : total_dist,
        "duration" : total_time,
        "steps" : steps,
        "total_fare" : total_fare
    }
    return jsonify(trip)

if __name__ == "__main__" :
    app.run('0.0.0.0',2000)


