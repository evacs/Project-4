from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine, Column, String, Integer, inspect, MetaData, Table
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)

db_path = 'sqlite:///movieRatings_1.db'
engine = create_engine(db_path)

# Metadata approach
metadata = MetaData()
metadata.autoload_with=engine

# Use automap_base to create a base with automapping capabilities
Base = automap_base()
Base.autoload_with=engine
inspector = inspect(engine)

# Extract column names from the columns object
columns = inspector.get_columns('top_movies')
column_names = [column['name'] for column in columns]
#print(column_names)

# # Get a list of table names in the database
# table_names = inspector.get_table_names()
# print("Tables in the database:")
# for table_name in table_names:
#     print(table_name)

#----------I DON'T THINK THIS WORKS, NO CLASSES AVAILBLE----------------
# Manually define the class for all tables
top_movies_table = Table('top_movies', metadata, autoload_with=engine)
class TopMovies(Base):
    __table__ = top_movies_table

movies_table = Table('movies', metadata, autoload_with=engine)
class Movies(Base):
    __table__ = movies_table

ratings_table = Table('ratings', metadata, autoload_with=engine)
class Ratings(Base):
    __table__ = ratings_table

# # Print out the mapped classes
# print('your keys:')
# print(Base.classes.keys())
# #print(dir(Ratings))
# # Create a connection
# # connection = engine.connect()

#------THIS WILL QUERY OUR TABLES----------------------------------
# # result = connection.execute(top_movies_table.select()).first()
# print(result)


@app.route('/')
def index():
    # Use SQLAlchemy's inspect function to get column names dynamically
    inspector = inspect(engine)
    columns = inspector.get_columns('top_movies')

    # Extract column names from the columns object
    column_names = [column['name'] for column in columns]

    print("Column Names:", column_names)  # Add this line for debugging

    # Pass the column names to the template
    return render_template('index.html', column_names=column_names)




if __name__ == '__main__':
    app.run(debug=True)