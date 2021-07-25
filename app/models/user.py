from ..extensions import lm, db
from flask_login import UserMixin

class User(db.Document, UserMixin):
    name = db.StringField()
    email = db.StringField()
    password = db.StringField()
    is_activated = db.BooleanField()
    avatar = db.URLField()
    
    def is_active(self):
        return is_activated

@lm.user_loader
def user_loader(user_id):
    return User.objects(pk=user_id).first()