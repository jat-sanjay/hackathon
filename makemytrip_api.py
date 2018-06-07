import requests

url = "https://www.makemytrip.com/pwa/framework/hotel/listing/scroll"

querystring = {
    "checkin":"07062018",
    "checkout":"07072018",
    "city":"RAJ",
    "country":"IN",
    "limit":"2500000",
    "roomCount":"1"
}

headers = {
    'cache-control': "no-cache",
    'postman-token': "49c30640-ecf8-98ee-df40-3253c4091145"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = response.json().get("data")
for item in data:
    hotel_id = item.get("data").get("hotel_id")
    hote_name = item.get("data").get("hotel_name")
    hotel_address1 = item.get("data").get("hotel_address").get("line1")
    hotel_address2 = item.get("data").get("hotel_address").get("line2")
    hotel_address =""
    if hotel_address1 and hotel_address2:
        hotel_address = hotel_address1 + hotel_address2
    elif hotel_address1:
        hotel_address = hotel_address1
    elif hotel_address2:
        hotel_address = hotel_address2
    else:
        hotel_address = "No address of this hotel"

    print (hotel_address)



