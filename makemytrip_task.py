import requests
import csv

BASEURL = "https://dtr-hoteldom.makemytrip.com/mmthtl/site/getMoreReviewsNew"
HOTEL_RECORDS = {
    "The Chancery Pavilion": 200701121638544369,
    "More hotels here....": -1
} # Global record for our hotels to keep the relation between hotel name and id.


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

    except Exception as e:
        print(e)

    return


def driver(hotel_name):
    """
    :param hotel_name: Name of the hotel to fetch reviews for.
    :return: None, writes a csv file on disk in same directory as <hotel_name>.csv
    """

    hotel_id = HOTEL_RECORDS.get(hotel_name)

    with open(hotel_name + '.csv', 'a') as f:
        all_review = get_all_reviews(hotel_id)  # use num_reviews for a subset of reviews, else it will fetch all.
        print("\n### Found {len} records for {hotel} ###\n".format(len=len(all_review), hotel=hotel_name))
        w = csv.DictWriter(f, all_review[0].keys())  # to add a header for csv
        w.writeheader()
        for review in all_review:
            w.writerow(review)


if __name__ == '__main__':
    driver(hotel_name="The Chancery Pavilion")
