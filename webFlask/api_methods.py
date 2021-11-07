from webFlask import main_functions
import requests

def request_key():
    apiList = main_functions.read_from_file("webFlask/JSON_Files/api_keys.json")
    return apiList ['my_key']

def request_best_sellers(timeFrame, category):
    url = "https://api.nytimes.com/svc/books/v3/lists/" + category + "/" + timeFrame + ".json?api-key=" + request_key()
    response = requests.get(url).json()
    return response

def request_book_reviews(bookTitle):
    url2 = "https://api.nytimes.com/svc/books/v3/reviews.json?title=" + bookTitle + "&api-key=" + request_key()
    response2 = requests.get(url2).json()
    return response2
