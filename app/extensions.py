from flask_login import LoginManager
from flask_mail import Mail
from flask_mongoengine import MongoEngine
db = MongoEngine()
mbox = Mail()
lm = LoginManager()