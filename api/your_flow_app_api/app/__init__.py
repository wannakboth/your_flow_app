from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    
    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)
    
    return app
