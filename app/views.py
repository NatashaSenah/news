from flask import render_template
from app import app
from .request import get_news
from .request import get_news,get_news

# Views
@app.route('/')
def index():
    general_news = get_news('general')
    business_news=get_news('business')
    technology_news=get_news('technology')
    sports_news=get_news('sports')
    entertainment_news=get_news('entertainment')
   
    title = 'Home - Welcome to The best News Highlight Website Online'
    return render_template('index.html', title = title, general = general_news,business=business_news,technology=technology_news,sports=sports_news,entertainment=entertainment_news)


@app.route('/news/<int:news_id>')
def news(news_id):
    news=get_news(id)
    title  = f'You are viewing{news_id}'
    return render_template('news.html',id = news_id)
