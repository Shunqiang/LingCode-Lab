from flask_login import login_required
from routes import  app
from flask import flash, redirect, render_template, request, url_for
from forms.article_form import ArticleForm
from models.article import Article
from services.article_service import ArticleService

@app.route('/createarticle.html', methods=['GET','POST'])
@login_required
def create_article_page():
    form = ArticleForm()
    if form.validate_on_submit():
        new_article = Article()
        new_article.title = form.title.data
        new_article.content = form.content.data
        try:
            article, error_msg = ArticleService().create_article(new_article)
            
            print(error_msg)
            if error_msg:
                flash(message= f'发布文章错误: {error_msg}', category='danger')
            else:
                flash(f'Article created successfully', category='success')
                return redirect(url_for('home_page'))
        except Exception as error:
            flash(f'发布文章错误: {error_msg}', category='message')
    return render_template('editarticle.html',form=form, is_edit=False)

@app.route('/editarticle/<article_id>.html', methods=['GET','POST'])
@login_required
def edit_article_page(article_id: str):
    form = ArticleForm()
    if request.method == 'GET':
        try:
             article = ArticleService().get_article(int(article_id))
             if not article:
                flash(f'没有找到文章: {error_msg}', category='message')
                return redirect(url_for('home_page'))
             else:
                 form.title.data = article.title
                 form.content.data = article.content
        except Exception as error:
            flash(f'没有找到文章: {error_msg}', category='message')
            return redirect(url_for('home_page'))
            
    if form.validate_on_submit():
        try:
            updated_article = Article()
            updated_article.title = form.title.data
            updated_article.content = form.content.data
            updated_article.id = int(article_id)
       
            article, error_msg = ArticleService().update_article(updated_article)
            print(error_msg)
            if error_msg:
                flash(message= f'编辑文章错误: {error_msg}', category='danger')
            else:
                flash(f'Article edited successfully', category='success')
                return redirect(url_for('home_page'))
        except Exception as error:
            flash(f'发布文章错误: {error_msg}', category='message')
    return render_template('editarticle.html',form=form,is_edit=True)
