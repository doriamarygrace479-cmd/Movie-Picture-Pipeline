from flask import jsonify
from flask.views import MethodView

# Dummy database to hold movie examples
movies = {
    "123": {"title": "Top Gun: Maverick", "description": "Fighter planes"},
    "456": {"title": "Sonic the Hedgehog", "description": "Blue Sega character"},
    "789": {"title": "A Quiet Place", "description": "Scary monsters"},
    "110": {"title": "Fast and Furious", "description": "action movie"},
    "1102": {"title": "V", "description": "movie"},
    "11044": {"title": "V2", "description2": "movie2"},
    "11045": {"title": "V4", "description2": "movie3"},
    "11046": {"title": "V3", "description2": "movie4"},
    "11047": {"title": "V23", "description2": "movie32"},
    "11048": {"title": "V2ssss", "description2": "movie3sss"},
}


class Movies(MethodView):
    def get(self, movie_id):
        if movie_id is None:
            # Return a list of all movies
            movies_data = [
                dict({"title": movie["title"]}, **{"id": i})
                for i, movie in movies.items()
            ]
            response_data = {"movies": movies_data}
            return jsonify(response_data)
        else:
            # Return the details of a specific movie
            return jsonify({"movie": movies[str(movie_id)]})
