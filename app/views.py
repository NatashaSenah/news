from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():
    general_news = get_news('general')
   
    title = 'Home - Welcome to The best News Highlight Website Online'
    return render_template('index.html', title = title, general = general_news)

    
@app.route('/news/<int:news_id>')
def news(news_id):
    return render_template('news.html',id = news_id)
