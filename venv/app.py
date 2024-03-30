from flask import Flask, request, render_template, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pepe1@localhost/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] ='lolo'

connect_db(app)
app.app_context().push()

@app.route('/')
def Home_Page():
    users = User.query.all()
    return render_template('home.html',users=users)

@app.route('/<int:user_id>')
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('details.html',user = user)

@app.route('/user_create')
def show_create():
    return render_template('create.html')

@app.route('/user_create',methods=['POST'])
def create_user():
    First_Name = request.form['First_Name']
    Last_Name = request.form['Last_Name']
    Profile_Pic = request.form['Profile_Pic']
    
    new_user = User(First_Name=First_Name, Last_Name=Last_Name, Profile_Pic=Profile_Pic)
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(f'/{new_user.id}')

@app.route('/delete',methods=['POST'])
def delete_user():
    user = request.form['id']
    User.query.filter(User.id == user).delete()
    db.session.commit()

    return redirect('/')

@app.route('/edit')
def show_edit():
    user_id= request.args['id']
    user=User.query.get(user_id)
    return render_template('edit.html',user=user)

@app.route('/edit',methods=['POST'])
def edit_user():
    user_id= request.form['id']
    First_Name = request.form['First_Name']
    Last_Name = request.form['Last_Name']
    Profile_Pic = request.form['Profile_Pic']
    
    User.query.get(user_id).First_Name=First_Name
    User.query.get(user_id).Last_Name=Last_Name 
    User.query.get(user_id).Profile_Pic=Profile_Pic
    db.session.commit()
    
    return redirect('/')