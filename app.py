# imports-----------------------------------/
from flask import (
  Flask,
  request,
  jsonify,
  abort
)
import os
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from models import setup_db, Movie, Actor
from auth.auth import AuthError, requires_auth
from jose import jwt
import json
# -------------------------------------------\

# config-------------------------------------/
MODELS_PER_PAGE = 10


def paginate_model(request, selection):
    if request:
        page = request.args.get('page', 1, type=int)
    else:
        page = 1
    start = (page-1)*MODELS_PER_PAGE
    end = start + MODELS_PER_PAGE
    models = [m.format() for m in selection]
    current_models = models[start:end]
    return current_models


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    cors = CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS')
        return response
    # ------------------------------------------\

    # Routes(Endpoints)-------------------------/
    # general end point
    @app.route('/')
    def index():
        return jsonify({
            "success": True,
            "Project":
            "Hello , This is the last FSND project .. ! wooho o o  o"
        })

    # ----1:GET /actors and /movies
    @app.route('/actors', methods=['GET'])
    def get_actors():
        actors = Actor.query.all()
        return jsonify({
            'success': True,
            'actors': [actor.format() for actor in actors]
        }), 200

    @app.route('/movies', methods=['GET'])
    def get_movies():
        movies = Movie.query.all()
        return jsonify({
            'success': True,
            'movies': [movie.format() for movie in movies]
        }), 200

    # ----2:DELETE /actors/ and /movies
    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(token, actor_id):
        actor = Actor.query.get(actor_id)
        if actor is None:
            abort(404)
        try:
            actor.delete()
        except Exception:
            db.session.rollback()
            abort(500)
        return jsonify({
                'success': True,
                'actor_id': actor_id,
                'message': 'actor info has been Deleted successfully'
         }), 200

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(token, movie_id):
        movie = Movie.query.get(movie_id)
        if movie is None:
            abort(404)
        try:
            movie.delete()
        except Exception:
            db.session.rollback()
            abort(500)
        return jsonify({
                'success': True,
                'movie_id': movie_id,
                'message': 'Movie info has been Deleted successfully'
        }), 200

    # ----3:POST /actors and /movies
    @app.route('/actors/create', methods=['POST'])
    @requires_auth('post:actors')
    def creat_new_actor(token):
        body = request.get_json()

        name = body['name']
        age = body['age']
        gender = body['gender']
        movieid = body['movieid']

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
    def create_new_movie(token):
        body = request.get_json()

        title = body['title']
        release_date = body['release_date']

        movie = Movie(title=title, release_date=release_date)
        movie.insert()

        newmovie = Movie.query.get(movie.id)
        newmovie = newmovie.format()
        return jsonify({
            'success': True,
            'created': movie.id,
            'newmovie': newmovie,
            'message': 'New Movie has been created successfully'
        })

    # ----4:PATCH /actors/ and /movies
    @app.route('/actors/update/<int:actor_id>', methods=['PATCH'])
    @requires_auth('update:actors ')
    def update_actor(token, actor_id):
        body = request.get_json()
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        actor.name = body['name']
        actor.age = body['age']
        actor.gender = body['gender']
        actor.movieid = body['movieid']
        actor.update()
        return jsonify({
            'success': True,
            'message': 'Actor info has been Updated successfully',
            'actor': actor.format()
        })

    @app.route('/movies/update/<int:movie_id>', methods=['PATCH'])
    @requires_auth('update:movies')
    def update_movie(token, movie_id):
        body = request.get_json()
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        title = body['title']
        release_date = body['release_date']
        movie.title = title
        movie.release_date = release_date
        movie.update()
        return jsonify({
            'success': True,
            'message': 'Movie info has been Updated successfully',
            'movie': movie.format()
        })
    # ------------------------------------------\

    # ErrorHandling----------------------------/
    @app.errorhandler(401)
    def not_authorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Authentication Error."
            }), 401

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method Not Allowed"
            }), 405

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Forbidden."
        }), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found."
            }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Request could not be processed."
            }), 422

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
# ------------------------------------------\
