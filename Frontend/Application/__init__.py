
from application import app

# MAKE SURE TO SET KEY AS AN ENV
# app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'


if __name__=='__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)