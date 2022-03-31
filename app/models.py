from flask_sqlalchemy import SQLAlchemy

# DB icin herhangi bir isim ver ve yarat
db = SQLAlchemy()

# Tools for DB
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from uuid import uuid4 #generating id 

# import and  create instanse of login manager
from flask_login import LoginManager, UserMixin #usermix'ini unutma
login = LoginManager()

# Necessary function for login manager
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin): #defining database columns, bildigimiz User table'i
    # lay out our columns just like we would in a SQL create table query
    # column_name = db.Column(db.DataType(<options>), constraints)
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True) # usrname column name
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    # This init method accepts input from user register form and transform that the way we can store to db
    def __init__(self,username, email, password, first_name='', last_name=''): 
        self.username= username
        self.email = email.lower()
        self.first_name = first_name
        self.last_name = last_name
        self.password = generate_password_hash(password) #once parantez icinceki salt and hash sonra diger self.password hits the database
        self.id = str(uuid4())
        
        
