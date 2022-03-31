from flask import Flask
from config import Config

# import blueprints
from .blueprints.auth.routes import auth
#from .blueprints.api.routes import api

# imports for database stuff + login manager
from .models import db, login
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(auth)
#app.register_blueprint(api)

# set up our ORM and Migrate connections
db.init_app(app)
migrate = Migrate(app, db)

#set up login manager
login.init_app(app)
login.login_view ='auth.signin'
login.login_message = 'Please sign in to see this page.'
login.login_message_category = 'danger'


from . import routes
from . import models