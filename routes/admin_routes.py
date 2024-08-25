from routes import  app
from flask import render_template

@app.route('/create_article')
def create_article():
    return render_template('index.html',title='create_article', content='create_article')
