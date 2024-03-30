from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)


  
class User(db.Model):
  __tablename__ ='Users'
  
  id=db.Column(db.Integer,
               primary_key=True,
               autoincrement=True)
  
  First_Name = db.Column(db.String(20),
                     nullable=False,)
  
  Last_Name = db.Column(db.String(20),
                     nullable=False,)
  
  Profile_Pic = db.Column(db.String(2000),
                     nullable=False,)