from flask import Flask, redirect, request, url_for,render_template,jsonify
from application import app, db, models
from application.models import Users
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import requests


@app.route('/')
def hello():
  data1 = Users.query.all()
  return render_template('home.html', data1=data1)


# registration: request username & password pair submission - post to db
# generate seed phrase: request 12 word output - post to db


# login: request request username & password pair submission

# transact: use username/password pair 


