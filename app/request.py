from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

base_url = app.config["NEWS_API_BASE_URL"]
def get_news(category):
    
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results
def process_results(news_list):
    
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        author = news_item.get('author')
        name = news_item.get('name')
        description = news_item.get('description')
        

        if name:
            news_object = News(id,author,name,description)
            news_results.append(news_object)

    return news_results
# def get_news(id):
#     get_news_details_url = base_url.format(id,api_key)

#     with urllib.request.urlopen(get_news_details_url) as url:
#         news_details_data = url.read()
#         news_details_response = json.loads(movie_details_data)

#         news_object = None
#         if news_details_response:
#             id = news_details_response.get('id')
#             title = movie_details_response.get('original_title')
#             overview = movie_details_response.get('overview')
#             poster = movie_details_response.get('poster_path')
#             vote_average = movie_details_response.get('vote_average')
#             vote_count = movie_details_response.get('vote_count')

#             movie_object = Movie(id,title,overview,poster,vote_average,vote_count)

#     return movie_object