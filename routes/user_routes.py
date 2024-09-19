from flask_login import logout_user
from routes import  app
from flask import abort, flash, redirect, render_template, url_for
from services.article_service import ArticleService
from forms.login_form import LoginForm
from services.user_service import UserService
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

@app.route('/login.html', methods=['POST', 'GET'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        result = UserService().do_login(username=form.username.data, password=form.password.data)
        if result:
            flash(f'欢迎回来', category='success')
            return redirect(url_for('home_page'))
        else:
            flash(f'账号密码错误', category='danger')
            
    return render_template('login.html', form=form)

@app.route('/logout.html')
def logout_page():
    logout_user()
    return redirect(url_for('home_page'))