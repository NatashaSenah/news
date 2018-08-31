from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
def index():
    title_news = get_news('title')
    author_news=get_news('author')
    description_news=get_news('description')
    title = 'Home - Welcome to The best News Highlight Website Online'
    return render_template('index.html', title = title,title = title_news,author=author_news,description=description_news)
@app.route('/news/<int:news_id>')
def news(news_id):
    return render_template('news.html',id = news_id)
