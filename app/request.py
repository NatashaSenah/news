from app import app
import urllib.request,json
from .models import news

News = news.News
Articles=news.Articles
article_url=app.config['ARTICLES_BASE_URL']
# Getting api key
api_key = app.config['NEWS_API_KEY']
articles_url=app.config['ARTICLES_BASE_URL']
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
        name = news_item.get('name')
        description = news_item.get('description')
        category=news_item.get('category')
        country=news_item.get('country')

        if name:
            news_object = News(id,name,description,category,country)
            news_results.append(news_object)

    return news_results
def get_brief(id):
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            description = news_details_response.get('description')
            category = news_details_response.get('category')
            country = news_details_response.get('country')
            

            news_object = News(id,name,description,category,country)

    return news_object
def get_new(news_id,limit):
   '''
   Function that gets the json response to our url request
   '''
   get_articles_url = article_url.format(news_id,limit,api_key)
   print(get_articles_url)

   with urllib.request.urlopen(get_articles_url) as url:
       get_articles_data = url.read()
       get_articles_response = json.loads(get_articles_data)

       articles_results = None

       if get_articles_response['articles']:
           articles_results_list = get_articles_response['articles']
           articles_results = process_articles(articles_results_list)

   return articles_results
def get_articles(source_id, limit):
    """
    Function that gets articles based on the source id
    """
    get_article_location_url = articles_url.format(source_id, limit, apiKey)

    with urllib.request.urlopen(get_article_location_url) as url:
        articles_location_data = url.read()
        articles_location_response = json.loads(articles_location_data)

        articles_location_results = None

        if articles_location_response['articles']:
            articles_location_results = process_articles(articles_location_response['articles'])

    return articles_location_results
def process_articles(news):
   source_articles = []
   for item_article in news:
       author = item_article.get('author')
       title = item_article.get('title')
       description = item_article.get('description')
       url = item_article.get('url')
       urlToImage = item_article.get('urlToImage')
       publishedAt = item_article.get('publishedAt')
       if urlToImage:
           articles_object = Articles(author,title,description,url,urlToImage,publishedAt)
           source_articles.append(articles_object)
   return source_articles
