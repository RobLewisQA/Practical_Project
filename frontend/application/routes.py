from flask import Flask, redirect, request, url_for,render_template
from application import app, db, models
from application.models import Users


@app.route('/')
def hello():
  data1 = Users.query.all()
  return render_template('home.html', data1=data1)


@app.route('/users/add', methods=['GET','POST'])
def add_user():
    return render_template('add_user.html')

@app.route('/add',methods=['GET','POST'])
def add_users():
    if request.method=='POST':
        new_first_name = request.form['first_name']
        new_last_name = request.form['last_name']
        new_email = request.form['email']
        new_number = 1
        new_user = Users(first_name=new_first_name,last_name=new_last_name,email=new_email,rand_number=new_number)
        db.session.add(new_user)
        db.session.commit()
        #data = Users.query.
        return redirect(url_for('hello'))

