from flask import Flask, jsonify, render_template
from sqlalchemy import create_engine, text, func, extract
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

app = Flask(__name__)


db_url = 'movieRatings.db'

engine = create_engine(db_url)

# Reflect an existing database and tables
Base = automap_base()
Base.prepare(autoload_with=engine)

session = Session(engine)

print('Connected to database and session initiated')

# Define static routes

# Launches site
@app.route('/') 
def index():
    return render_template('index.html')

@app.route('/bias')
def get_data_bias():
