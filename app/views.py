from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    message = 'NEWS HIGHLIGHT'
    return render_template('index.html',message = message)
@app.route('/news/<int:news_id>')
def news(news_id):
    return render_template('news.html',id = news_id)
