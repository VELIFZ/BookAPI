from flask_sqlalchemy import SQLAlchemy

# DB icin herhangi bir isim ver ve yarat
db = SQLAlchemy()

# Tools for DB
from datetime import datetime, timezone
from werkzeug.security import generate_password_hash
from uuid import uuid4 #generating id 
from secrets import token_hex

# import and  create instanse of login manager
from flask_login import LoginManager, UserMixin #usermix'ini unutma
login = LoginManager()

# Necessary function for login manager
@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin): 
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True) # usrname column name
    email = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    password = db.Column(db.String(250), nullable=False)
    api_token = db.Column(db.String(35))
    posts = db.relationship('Post', backref='author')
    seller = db.relationship('Book', backref=db.backref('sellers'))
    # profile_pic = db.Column(db.String(20), nullable=False, default='default.jpg')
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    

    # This init method accepts input from user register form and transform that the way we can store to db
    def __init__(self,username, email, password, first_name='', last_name=''): 
        self.username= username
        self.email = email.lower()
        self.first_name = first_name
        self.last_name = last_name
        self.password = generate_password_hash(password) #once parantez icinceki salt and hash sonra diger self.password hits the database
        self.id = str(uuid4())

    def generate_token(self):
        self.api_toke = token_hex(16)


# create table for forum posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    body = db.Column(db.String(300))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.String, db.ForeignKey('user.id')) # nullable=False
    
        
##
# New DB model for Book API
class Book(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey('user.id')) 
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    condition = db.Column(db.String(50), default=True, nullable=False)
    description = db.Column(db.String(300))
    price = db.Column(db.Float(2), nullable=False)
    image = db.Column(db.String(200))
    publisher = db.Column(db.String(50))
    publish_year = db.Column(db.String(50))
    categories = db.Column(db.String(50)) 
    stock = db.Column(db.Float(2), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    # when a user submits a POST request to create a new animal, they'll be sending us a python dictionary, we'll then use that to make our object
    def __init__(self, dict):
        self.id = str(uuid4())
        self.user_id = dict.get('user_id')
        self.title = dict['title'].title()
        self.author = dict['author'].title()
        self.condition = dict['condition']
        self.description = dict.get('description')
        self.image = dict.get('image')
        self.price = dict['price']
        self.publisher = dict.get('publisher').title()
        self.publish_year = dict.get('publish_year')
        self.categories = dict.get('categories')
        self.date_posted = dict.get('date_posted')
        self.stock = dict['stock']

    # write a function to translate this object to a dictionary
    # role here is take self and return a dictionary containing K:V pairs for each attribute
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'author': self.author,
            'condition': self.condition,
            'description': self.description,
            'image': self.image,
            'price': self.price,
            'publisher': self.publisher,
            'publish_year': self.publish_year,
            'categories': self.categories,
            'date_posted': self.date_posted,
            'stock': self.stock
        }

    def from_dict(self, dict):
        """
        works for the update route - accepts the dictionary provided by the request and updates the book with any present keys
        """
        if dict.get('title'):
            self.title = dict['title'].title()
        if dict.get('author'):
            self.author = dict['author'].title()
        if dict.get('condition'):
            self.condition = dict['condition']
        if dict.get('description'):
            self.description = dict['description']
        if dict.get('image'):
            self.image = dict['image']
        if dict.get('price'):
            self.price = dict['price']
        if dict.get('publisher').title():
            self.publisher = dict['publisher']
        if dict.get('publish_year'):
            self.publish_year = dict['publish_year']
        if dict.get('categories'):
            self.categories = dict['categories']
        if dict.get('date_posted'):
            self.date_posted = dict['date_posted']
        if dict.get('stock'):
            self.stock = dict['stock']
        
        

