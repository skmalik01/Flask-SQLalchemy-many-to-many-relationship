from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///many_to_many.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

user_channel = db.Table("user_channel",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("channel_id", db.Integer, db.ForeignKey("channel.id"))       
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    following = db.relationship("Channel", secondary=user_channel, backref="followers")
    
    def __repr__(self) -> str:
        return f"<User : {self.name}>"
    
class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    
    def __repr__(self) -> str:
        return f"<Channel : {self.name}>"