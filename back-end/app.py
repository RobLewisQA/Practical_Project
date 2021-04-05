from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from application import app


if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)