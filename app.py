# @app.route('/')
# def index():
#     movie_categories = ["Action", "Adventure","Animation","Children's","Comedy", "Crime", "Documentary", "Drama","Fantasy","Film-Noir", "Horror",
#                         "Musical","Mystery","Romance","Sci-Fi","Thriller", "War","Western"]

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movieRatings.db'
# C:\Users\evacs\Desktop\Class Repos\Project-4-MovieRec\movieRatings.db
# db_path = 'sqlite:///movieRatings.db'
# engine = create_engine(db_path)
#Movies = Base.classes.result  # Movies to be recommended
 #Movies to be rated
# ---------------------------------------------------------------------------
# from flask import Flask, jsonify, render_template, request
# from sqlalchemy import create_engine, Column, String, Integer, inspect
# from sqlalchemy.orm import declarative_base, Session
# from sqlalchemy.ext.automap import automap_base


# app = Flask(__name__)


# db_path = 'sqlite:///movieRatings.db'
# engine = create_engine(db_path)

# Base = automap_base()
# # reflect the tables
# Base.prepare(autoload_with=engine)

# session = Session(engine)
# TopMovies = Base.classes.top_movies


# # Create an Inspector object to inspect the database
# inspector = inspect(engine)

# # Get a list of table names in the database
# table_names = inspector.get_table_names()
# print("Tables in the database:")
# for table_name in table_names:
#     print(table_name)




# # class Result(Base):
# #     __tablename__ = 'top_movies'

# #     id = Column(Integer, primary_key=True)
# #     genre = Column(String(50), unique=True, nullable=False)
# #     movie1 = Column(String(100), nullable=False)
# #     movie2 = Column(String(100), nullable=False)
# #     movie3 = Column(String(100), nullable=False)
# #     movie4 = Column(String(100), nullable=False)
# #     movie5 = Column(String(100), nullable=False)

# #engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
# #Base.metadata.create_all(engine)



# # Home route
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Test route
# @app.route('/test_db')
# def test_db():
#     try:
#         session = Session(engine)
#         TopMovies = Base.classes.top_movies
#         result = session.query(TopMovies).first()
#         session.close()

#         genre = ["Action", "Adventure","Animation","Children's","Comedy", "Crime", "Documentary", "Drama","Fantasy","Film-Noir",\
#              "Horror","Musical","Mystery","Romance","Sci-Fi","Thriller", "War","Western"]
    

#         if result:
#             return f"Database connection successful. Sample data: Genre - {TopMovies.first()}"
#         else:
#             return "No data found in the database."
#     except Exception as e:
#         return f"Error connecting to the database: {str(e)}"

# # Route to get movies based on selected genre
# @app.route('/get_movies', methods=['POST'])
# def get_movies():
#     selected_genre = request.form['genre']
#     session = Session(engine)
#     result = session.query(Result).filter_by(genre=selected_genre).first()
#     session.close()

#     if result:
#         movies = [result.movie1, result.movie2, result.movie3, result.movie4, result.movie5]
#         return jsonify({'movies': movies})
#     else:
#         return jsonify({'error': 'Genre not found'})

# # Route to receive movie ratings
# @app.route('/rate_movies', methods=['POST'])
# def rate_movies():
#     ratings = request.form.getlist('ratings[]')
#     # You can process the ratings as needed, store in the database, etc.
#     # For simplicity, let's just print the ratings for now.
#     print(ratings)
#     return jsonify({'message': 'Ratings submitted successfully'})

# # Route to recommend movies
# @app.route('/recommend_movies', methods=['POST'])
# def recommend_movies():
#     # Add your movie recommendation logic using your AI model here
#     # For now, let's return dummy recommendations
#     recommendations = ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E']
#     return jsonify({'recommendations': recommendations})

# if __name__ == '__main__':
#     app.run(debug=True)
# # ---------------------------------------------------------------------------------------

from flask import Flask
from sqlalchemy import create_engine, inspect, MetaData, Table
from sqlalchemy.orm import Session, declarative_base
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)

db_path = 'sqlite:///movieRatings.db'
engine = create_engine(db_path)

# Use automap_base to create a base with automapping capabilities
Base = automap_base()
Base.prepare(engine, reflect=True)


# # Manually exclude 'result' table
# if 'result' in Base.classes:
#     del Base.classes['result']

# Print out the mapped classes
print('your keys:')
print(Base.classes.keys())


# TopMovies = Base.classes.top_movies

inspector = inspect(engine)
columns = inspector.get_columns('top_movies')
# Get a list of table names in the database
table_names = inspector.get_table_names()
print("Tables in the database:")
for table_name in table_names:
    print(table_name)

# Manually define the class for 'top_movies'
metadata = MetaData()
top_movies_table = Table('top_movies', metadata, autoload_with=engine)

class TopMovies(Base):
    __table__ = top_movies_table

# TopMovies = Base.classes.top_movies

class Links(Base):
    __table__ = Base.metadata.tables['links']



session = Session(engine)

# TopMovies = Base.classes.links
Movies = Base.classes.result

# Print classes and tables for debugging
print("Classes in Base:", Base.classes.keys())
print("Tables in metadata:", Base.metadata.tables.keys())

column_names = [column.name for column in TopMovies.__table__.columns]
print("Column names in TopMovies class:", column_names)

print("columns in result: ", Movies.keys())

# action =  session.query(TopMovies).first()
# print("first column in top movies:", action)
#print("Keys in top_movies?:", TopMovies.keys())
#print("Tables in metadata:", Base.metadata.tables.keys())

# Test route
# @app.route('/')
# def test_db():
#     try:
#         # Query the first row from the TopMovies table
#         top_movie_instance = session.query().first()

#         if top_movie_instance:
#             return f"Database connection successful."
#         else:
#             return "No data found in the database."
#     except Exception as e:
#         return f"Error connecting to the database: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

# # Test route
# @app.route('/')
# def test_db():
#     try:
#         # Inspect the table and get column names
#         inspector = inspect(engine)
#         columns = inspector.get_columns('top_movies')  # Replace 'top_movies' with your actual table name

#         # Extract column names
#         column_names = [column['name'] for column in columns]

#         return jsonify({"columns": column_names})
#     except Exception as e:
#         return jsonify({"error": f"Error connecting to the database: {str(e)}"})

# if __name__ == '__main__':
#     app.run(debug=True)
