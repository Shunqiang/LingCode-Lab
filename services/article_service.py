from routes import db
from models.article import Article
from sqlalchemy import Select, and_, func

class ArticleService:
    def get_article(self, id):
        return db.session.get(Article, id)
    
    def get_articles(self):
       query = Select(Article)
       return db.session.scalars(query).all()
   
    def create_article(self, article: Article):
        query = Select(Article).where(Article.title == article.title)
        exit_articles = db.session.scalars(query).first()
        
        print(exit_articles)
        if exit_articles:
            return article, '同标题的文章已经存在'
        
        db.session.add(article)
        db.session.commit()
        return article, None
    def update_article(self, article: Article):
        exist_articles = db.session.get(Article, article.id)
        if not exist_articles:
            return article, '文章不存在'
        
        query = Select(Article).where(and_(Article.id != article.id, Article.title == article.title))
        same_title = db.session.scalars(query).add()
        if same_title:
            return article, '同标题的文章已存在'
                                      
                                       
        exist_articles.title =  article.title
        exist_articles.content =  article.content
        exist_articles.update_time =  func.now()
        
        db.session.commit()
        
        return article, None
    
    