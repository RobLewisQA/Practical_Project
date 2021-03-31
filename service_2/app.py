from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# Replace [PASSWORD] with the root password for your mysql container
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql:3306/flask-db'

#class entrants(db.Model):
#	id = db.Column(db.Integer, primary_key=True)
#	num1 = db.Column(db.String(30), nullable=False)
#	num2 = db.Column(db.String(30), nullable=False)
#	def __repr__(self):
#	  return ''.join(['id', str(self.id), '\r\n', 'num1', self.num1, 'num2', self.num2])


@app.route('/')
def hello():
  data1 = entrants.query.all()
  return str('Hello all!')

if __name__=='__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)


# @app.route('/')
# def random_number():
#     rand_num = ''
#     for n in range(5):
#         n = rand_num + str(random.randint(1,9))
#     return rand_num

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@mysql:3306/flask-db'

# @app.route('/')
# def hello():
#   data1 = Users.query.all()
#   return str(data1)


# if __name__=='__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)