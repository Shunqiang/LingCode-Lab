from routes import  app
from flask import flash, redirect, render_template, url_for
from forms.article_form import ArticleForm
from models.article import Article
from services.article_service import ArticleService

@app.route('/editarticle.html', methods=['GET','POST'])
def create_article_page():
    form = ArticleForm()
    if form.validate_on_submit():
        new_article = Article()
        new_article.title = form.title.data
        new_article.content = form.content.data
        try:
            ArticleService().create_article(new_article)
            flash(f'Article created successfully', category='success')
            return redirect(url_for('home_page'))
        except Exception as error:
            flash(error, category='error')
    return render_template('editarticle.html',form=form)
