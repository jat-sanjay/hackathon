import requests

url = "https://www.makemytrip.com/pwa/framework/hotel/listing/scroll"

querystring = {
    "checkin":"12062019",
    "checkout":"12072019",
    "city":"RAJ",
    "country":"IN",
    "limit":"2500000",
    "pageNumber":"1",
    "roomStayQualifier":"2e0e",
    "firstTimeUserState":"0",
    "loggedIn":"false",
    "trafficSrc":"null",
    "filters":"",
    "sorter":"",
    "lastFetchedHotelId":"201601081207013687",
    "isAllHotelsFetched":"false",
    "roomCount":"1"
}

headers = {
    'cache-control': "no-cache",
    'postman-token': "49c30640-ecf8-98ee-df40-3253c4091145"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)