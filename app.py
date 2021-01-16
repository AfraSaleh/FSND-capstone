#imports-----------------------------------/
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import setup_db, Movie, Actor
from auth.auth import AuthError, requires_auth
import os
from jose import jwt
import json
#-------------------------------------------\

#config-------------------------------------/
def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    """ ENV = 'dev '

    if ENV == 'dev':
        app.debug = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:afraa@localhost:5432/capstone'

    else:
        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = ''

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False """
    #------------------------------------------\

    #Routes(Endpoints)-------------------------/

    @app.route('/')
    def index():
        return jsonify({
            "success": True,
            "Project": "hii",
        })

    #----1:GET /actors and /movies
    @app.route('/actors', methods=['GET'])
    def GetActors():
        actors = Actor.query.all()
        if not actors:
            abort(404)
        return jsonify({
            'success': True,
            'actors': [actor.format() for actor in actors]
        }), 200
    
    @app.route('/movies', methods=['GET'])
    def GetMovies():
        movies = Movie.query.all()
        if not movies:
            abort(404)
        return jsonify({
            'success': True,
            'movies': [movie.format() for movie in movies]
        }), 200

    #----2:DELETE /actors/ and /movies
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def DeleteActor(token,actor_id):
        if not actor_id:
            abort(404)
        deleteactor = Actor.query.get(actor_id)
        if not deleteactor:
            abort(404)
        deleteactor.delete()
        return jsonify({
                'success': True,
                'actor_id': actor_id,
                'message': 'Actor info has been Deleted successfully'
        }), 200

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def DeleteMovie(token, movie_id):
        if not movie_id:
            abort(404)
        deletemovie = Movie.query.get(movie_id)
        if not deletemovie:
            abort(404)
        deletemovie.delete()
        return jsonify({
                'success': True,
                'movie_id': movie_id,
                'message': 'Movie info has been Deleted successfully'
        }), 200

    #----3:POST /actors and /movies
    @app.route('/actors/create', methods=['POST'])
    @requires_auth('post:actors')
    def CreatNewActor(token):
        body = request.get_json()

        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        movieid = body.get('movieid', None)

        actor = Actor(name=name, age=age, gender=gender, movieid=movieid)
        actor.insert()
        newactor = Actor.query.get(actor.id)
        newactor = newactor.format()
        return jsonify({
            'success': True,
            'created': actor.id,
            'newactor': newactor,
            'message': 'New Actor has been created successfully'
        })

    @app.route('/movies/create', methods=['POST'])
    @requires_auth('post:movies')
    def CreateNewMovie(token):
        body = request.get_json()
        title = body.get('title', None)
        release_date = body.get('release_date', None)
        movie = Movie(title=title, releasedate=release_date)
        movie.insert()
        newmovie = Movie.query.get(movie.id)
        newmovie = newmovie.format()
        return jsonify({
            'success': True,
            'created': movie.id,
            'newmovie': newmovie,
            'message': 'New Movie has been created successfully'
        })

    #----4:PATCH /actors/ and /movies
    @app.route('/actors/update/<int:actor_id>', methods=['PATCH'])
    @requires_auth('update:actors ')
    def UpdateActor(token ,actor_id):
        body = request.get_json()
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        movieid = body.get('movieid', None)
        actor.update()
        return jsonify({
            'success': True,
            'message': 'Actor info has been Updated successfully',
        })

    @app.route('/movies/update/<int:movie_id>', methods=['PATCH'])
    @requires_auth('update:movies')
    def UpdateMovie(token, movie_id):
        body = request.get_json()
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        title = body.get('title', None)
        releasedate = body.get('releasedate', None)
        movie.title = title
        movie.releasedate = releasedate
        movie.update()
        return jsonify({
            'success': True,
            'message': 'Movie info has been Updated successfully'
        })
    #------------------------------------------\

    # ErrorHandling----------------------------/
    @app.errorhandler(401)
    def NotAuthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Authentication Error."
            }), 401
    @app.errorhandler(404)
    def NotFound(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found."
            }), 404
    @app.errorhandler(422)
    def Unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Request could not be processed."
            }), 422

    return app 


app = create_app()

if __name__ == '__main__':
    app.run()
#------------------------------------------\



