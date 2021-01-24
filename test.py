import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from flask import url_for
from models import setup_db, Movie, Actor

# -----------------------------------------------/
# when apply pycodestyle test.py
# this error will appear but token can not be seperated
# test.py:1:80: E501 line too long (860 > 79 characters)
TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImE3N05VZHZ4bC1veldYNVR5NEtmcCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZHNsa3htOC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWZmZGQwZTMzMjI1ZjkwMDc3Y2Y3NGFiIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MTE0ODQzODAsImV4cCI6MTYxMTQ5MTU4MCwiYXpwIjoidGRoMHdpY1dTajhrV2RYa1B6cE00Zm10NldHb2FuMmEiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyAiLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyIsInVwZGF0ZTphY3RvcnMgIiwidXBkYXRlOm1vdmllcyJdfQ.Fa4Om3WXTYM-AFoZe5rpwk3ftRiBVyYYjePzsL8yjArfrLlTxZXU1wC6N14NgbQKNPfLaQQwQAUFyCY7-fuRdG2R0GotA9we_t1fP6VgoM1DfG0DQoe275atNRCa1dTJ1JPipttkZzgq5qHIc0FT0fS8NsJXYwbxStSeCvS-K03zhW40mjhPvpFnxgiIisr6DUiFaBnPgha6jn0ScEuOIbwwq-OnMtgBYWGaI8w09dlIHj5N0FSwEMgTzIbCrf0MH3slfuW5uEq573-8TDAUYehNBcSRQeLSgAYkKr9-_zSb0CTQpMQYA88lnWTIUFu-f99CK1vFmNJ4CU-MIPJ2ow'


class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone"
        self.database_path = "postgres://{}@{}/{}".format(
            'postgres:afraa', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass
    # -----------------------------------------
    #################################################

    def test_get_actors(self):
        n_actor = Actor(name='fatima', age=30, gender='female', movieid=20)
        n_actor.insert()
        respo = self.client().get('/actors',
                                  headers={'Authorization':
                                           "Bearer " + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_refuse_get_actors(self):
        n_actor = Actor(name='fatima', age=30, gender='female', movieid=20)
        n_actor.insert()
        respo = self.client().post('/actors',
                                   headers={'Authorization':
                                            "Bearer " + TOKEN})
        self.assertEqual(respo.status_code, 405)
    #################################################

    def test_get_movies(self):
        n_movie = Movie(title='lala land', release_date='2091-01-13')
        n_movie.insert()
        respo = self.client().get('/movies',
                                  headers={'Authorization':
                                           "Bearer {}" + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_refuse_get_movies(self):
        n_movie = Movie(title='peewooo', release_date='2091-01-13')
        n_movie.insert()
        respo = self.client().post('/movies',
                                   headers={'Authorization':
                                            "Bearer {}" + TOKEN})
        self.assertEqual(respo.status_code, 405)
    #################################################

    def test_post_actor(self):
        self.NewActor = {
            "name": "sara",
            "age": 30,
            "gender": "female",
            "movieid": 20
        }
        respo = self.client().post('/actors/create',
                                   json=self.NewActor,
                                   headers={'Authorization':
                                            'Bearer ' + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['newactor']['name'], self.NewActor['name'])
        self.assertEqual(data['newactor']['age'], self.NewActor['age'])
        self.assertEqual(data['newactor']['gender'], self.NewActor['gender'])
        newactor = Actor.query.get(data['newactor']['id'])
        self.assertTrue(newactor)

    def test_refuse_create_new_actor(self):
        NewActor = {
            "name": "sara",
            "age": 30,
            "gender": "female",
            "movieid": 20
        }
        respo = self.client().post('/actors/post',
                                   data=json.dumps(NewActor),
                                   headers={'Authorization':
                                            "Bearer " + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertFalse(data['success'])
    #################################################

    def test_post_movies(self):
        self.NewMovie = {
            "title": "new movie posted",
            "release_date": "Mon, 03 Jan 2022 00:11:11 GMT"
        }
        respo = self.client().post('/movies/create',
                                   json=self.NewMovie,
                                   headers={'Authorization':
                                            'Bearer' + TOKEN})

        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['newmovie']['title'], self.NewMovie['title'])
        self.assertEqual(data['newmovie']['release_date'],
                         self.NewMovie['release_date'])
        newmovie = Actor.query.get(data['newmovie']['id'])

    def test_refuse_create_new_movie(self):
        NewMovie = {
            "title": "new movie posted",
            "release_date": "2091-01-13"
        }
        respo = self.client().post('/movies/post',
                                   data=json.dumps(NewMovie),
                                   headers={'Authorization':
                                            "Bearer " + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertFalse(data['success'])
    #################################################

    def test_update_actor(self):
        actor = Actor(name="sara", age=30, gender="female", movieid=20)
        actor.insert()
        self.updatedData = {
            'name': 'sara',
            'age': 30,
            'gender': 'female',
            'movieid': 20
        }
        respo = self.client().patch(f'/actors/update/%s' % (actor.id),
                                    json=self.updatedData,
                                    headers={'Authorization':
                                             "Bearer " + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actor']['name'], self.updatedData['name'])
        self.assertEqual(data['actor']['age'], actor.age)
        self.assertEqual(data['actor']['gender'], actor.gender)
        actorupdated = Actor.query.get(data['actor']['id'])
        self.assertEqual(actorupdated.id, actor.id)

    def test_refuse_update_actor(self):
        updatedData = {
            "name": 'abdullah',
            "age": 28
        }
        respo = self.client().patch('/actors/create/777',
                                    data=json.dumps(updatedData),
                                    headers={'Authorization':
                                             "Bearer " + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertFalse(data['success'])
    #################################################

    def test_delete_actors(self):
        actors = Actor(name="afraa", age=23, gender="female", movieid=20)
        actors.insert()
        actor_id = actors.id
        respo = self.client().delete(f'/actors/{actor_id}',
                                     headers={'Authorization':
                                              "Bearer " + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actor_id'], actors.id)

    def test_refuse_delete_actor(self):
        respo = self.client().delete('/actors/455010',
                                     headers={'Authorization':
                                              "Bearer " + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertFalse(data['success'])
    #################################################

    def test_update_movies(self):
        movies = Movie(title="old movie8888888",
                       release_date="Sat, 09 Jan 2091 00:00:00 GMT")
        movies.insert()
        self.updatedData = {
            "title": "old movie000000",
            "release_date": "Sat, 09 Jan 2091 00:00:00 GMT"
        }
        respo = self.client().patch(f'/movies/update/%s' % (movies.id),
                                    json=self.updatedData,
                                    headers={'Authorization':
                                             "Bearer " + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertTrue(data['success'])
        movieupdated = movies.query.get(data['movie']['id'])
        self.assertEqual(movieupdated.id, movies.id)

    def test_refuse_update_movie(self):
        updatedData = {
            "title": "ho",
            "release_date": "Sat, 09 Jan 2091 00:00:00 GMT"
        }
        respo = self.client().patch('/movies/update',
                                    json=json.dumps(updatedData),
                                    headers={'Authorization':
                                             "Bearer " + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertFalse(data['success'])
    #################################################

    def test_delete_movies(self):
        movies = Movie(title="its a movie title", release_date="2091-01-13")
        movies.insert()
        movie_id = movies.id
        respo = self.client().delete(f'/movies/{movie_id}',
                                     headers={'Authorization':
                                              "Bearer " + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['movie_id'], movies.id)

    def test_refuse_delete_movies(self):
        respo = self.client().delete('/movies/9999999',
                                     headers={'Authorization':
                                              "Bearer " + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertFalse(data['success'])
    #################################################

    def test_delete_acotr_executive_producer_token(self):
        respo = self.client().delete('/actors/8',
                                     headers={'Authorization':
                                              "Bearer " + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 404)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

    def test_delete_movie_executive_producer_token(self):
        respo = self.client().delete('/movies/2',
                                     headers={'Authorization':
                                              "Bearer " + TOKEN})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 404)
        self.assertFalse(data["success"])
        self.assertIn('message', data)

# ---------------------------------------------------/


if __name__ == "__main__":
    unittest.main()
