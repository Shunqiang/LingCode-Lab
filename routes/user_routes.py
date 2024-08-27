from routes import  app
from flask import abort, render_template
from services.article_service import ArticleService

@app.route('/')
@app.route('/index.html')
def home_page():
    articles = ArticleService().get_articles()
    print(1111222)
    
    if  articles:
        print(articles)
        return render_template('index.html', articles=articles)
    abort(404)

@app.route('/about')
def about_page():
    
    return 'about page'

@app.route('/article/<article_id>.html')
def get_article_page(article_id):
    article = ArticleService().get_article(article_id)
    if  article:
        return render_template('article.html', article=article)
    abort(404)

@app.route('/login.html')
def login_page():
    return 'login page'