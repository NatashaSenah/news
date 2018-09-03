from flask import render_template
from app import app
from .request import get_news
from .request import get_new,get_news

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

@app.route('/news/<string:id>&<int:page_size>')
def articles(id,page_size):

   articles = get_new(id,page_size)
   return render_template('news.html',articles=articles)