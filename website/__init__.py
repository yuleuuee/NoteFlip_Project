from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path 
from flask_login import LoginManager # help to manage login and related things



# ***************************


# Database:
db = SQLAlchemy()
DB_NAME = "database.db" 


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='ketirubbv adoidfknbsl' #just to ensript the cookie and session area
    
    #creating database by using sqlite Database
    # app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///{DB_NAME}"

    #creating database by using Mysql Database : Currently in use
    app.config['SQLALCHEMY_DATABASE_URI']= "mysql+pymysql://root:rabhav9861@localhost/Notefilp_users"



    db.init_app(app)

    from .views import views
    from .auth import auth
    
    # registering the Blueprints
    app.register_blueprint(views, url_prefix='/') # '/' means no prefix
    app.register_blueprint(auth, url_prefix='/')

    # from . import models
    from .models import User,Note 

    #after we create the database then -->
    # If the user is not logid in then we redirect him to "login page"
    login_manager =LoginManager()
    login_manager.login_view="auth.login"
    login_manager.init_app(app) 

    # telling flask how we load a user.
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # works similar to "filter by"
     

    create_database(app)
    return app



#-----------------------------
def create_database(app):
    with app.app_context():
        db.create_all()
        print('Created Database!')

# def create_database(app):
#     from .models import User, Note
#     if not path.exists('website/' + DB_NAME):
#         with app.app_context():
#             db.create_all()
#             print('Created Database!')


#             #getting all users from the database
#             all_users = User.query.all()

#              # Print user data to the console (for demonstration purposes)
#             for user in all_users:
#                 print(f"User ID: {user.id}, Email: {user.email}, First Name: {user.first_name}, Notes: {user.notes}")
