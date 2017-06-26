import os
from flask import Flask, render_template
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config.from_object(os.environ['APP_SETTINGS'])
#print(os.environ['APP_SETTINGS'])

#db = SQLAlchemy(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/catalogue')
def catalogue():
    return render_template('catalogue.html')

@app.route('/bike')
def showBike():
	return render_template('bike.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
