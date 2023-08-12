# app.py
from flask import Flask, jsonify
from movies_data import get_average_rating, get_highest_rated_film, get_lowest_rated_film

# Init app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'msg': 'Hello World!'})

@app.route('/movies-data', methods=['GET'])
def movie_data():
    average_rating = get_average_rating()
    highest_rated_film = get_highest_rated_film()
    lowest_rated_film = get_lowest_rated_film()

    response = {
        'average_rating': average_rating,
        'highest_rated_film_title': highest_rated_film['title'],
        'lowest_rated_film_year': lowest_rated_film['year']
    }
    
    return jsonify(response)

# Run Server
if __name__ == "__main__":
    app.run(debug=True)