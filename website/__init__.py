from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.secret_key = 'hfyurur rfu7ngg 4u78tyfur'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .auth import auth
    from .views import views
    from .backend import bck
    
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(bck, url_prefix='/')
    
    from .models import User
    with app.app_context():
        if not path.exists('website'+DB_NAME):
            db.create_all()
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

def update_site(user):
    from .models import Site
    from . import db
    site = Site.query.filter_by(name='site').first()
    if site:
        site.visits += 1
        if user.is_authenticated:
            site.unique_visits += 1
        db.session.commit()
    else:
        site = Site(name='site', visits=0, unique_visits=0)
        site.visits += 1
        site.unique_visits += 1
        db.session.add(site)
        db.session.commit()
    print(site.visits)
    print(site.unique_visits)