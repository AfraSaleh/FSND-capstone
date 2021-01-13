import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import setup_db, Movie, Actor

#-----------------------------------------------/
class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone"
        self.database_path = "postgres://postgres/afraa".format('localhost:5432', self.capstone)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
    
    def tearDown(self):
        pass
#-----------------------------------------
    def TestGetActors(self):
        respo = self.client().get('/actors')
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))
    def TestDeleteActors(self):
        actors = Actor(name="afraa", age="23", gender="female")
        actors.insert()
        actor_id = actors.id
        respo = self.client().delete(f'/actors/{actor_id}')
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actor_id'], actors.id)  
    def TestPostActor(self):
        NewActor = {
            "name": "sara",
            "age": 30,
            "gender": "female"
        } 
        respo = self.client().post('/actors/create', data=json.dumps(NewActor), headers={'Content-Type': 'application/json'})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actors']['name'], NewActor['name'])
        self.assertEqual(data['actors']['age'], NewActor['age'])
        self.assertEqual(data['actors']['gender'], NewActor['gender'])
        newactor = Actor.query.get(data['actors']['id'])
        self.assertTrue(newactor)
    def TestUpdateActor(self):
        actors = Actor(name="mohammed", age="50", gender="male")
        actors.insert()
        updatedData = {
            "name": "omar"
        } 
        respo = self.client().update(f'/actors/%s' % (actors.id), data=json.dumps(updatedData),headers={'Content-Type': 'application/json'})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['actors']['name'], updatedData['name'])
        self.assertEqual(data['actors']['age'], actor.age)
        self.assertEqual(data['actors']['gender'], actor.gender)
        actorupdated = Actor.query.get(data['actors']['id'])
        self.assertEqual(actorupdated.id, actors.id)
    def TestDelete_Notfound_Actor(self):
        respo = self.client().delete('/actors/455010')
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertFalse(data['success'])
    def TestUpdate_Notfound_Actor(self):
        updatedData = {
            "name": 'abdullah',
            "age": 28
        } 
        respo = self.client().update('/actors/update/777', data=json.dumps(updatedData), headers={'Content-Type': 'application/json'})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertFalse(data['success'])
    def TestDeleteAcotr_ExecutiveProducertoken(self):
        respo = self.client().delete('/actors/8', headers={'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 401)
        self.assertFalse(data["success"])
        self.assertIn('message', data) 


  #------------------------------------------
    def TestGetMovies(self):
        respo = self.client().get('/movies')
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies'])) 
    def TestDeleteMovies(self):
        movies = Movie(title="its a movie title", releasedate="20-10-2018")
        movies.insert()
        movie_id = movies.id
        respo = self.client().delete(f'/movies/{movie_id}')
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['movie_id'], movies.id)  
    def TestPostMovies(self):
        NewMovie = {
            "title": "new movie posted",
            "releasedate": "30-12-2020"
        } 
        respo = self.client().post('/movies/create', data=json.dumps(NewMovie), headers={'Content-Type': 'application/json'})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['movies']['title'], NewMovie['title'])
        self.assertEqual(data['movies']['releasedate'], NewMovie['releasedate'])
        newmovie = Actor.query.get(data['movies']['id'])
        self.assertTrue(newmovie)
    def TestUpdateMovies(self):
        movies = Actor(title="old movie", releasedate="10-11-2012")
        movies.insert()
        updatedData = {
            "releasedate" : "10-11-2009"
        } 
        respo = self.client().update(f'/movies/%s' % (movies.id), data=json.dumps(updatedData),headers={'Content-Type': 'application/json'})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['movies']['name'], updatedData['name'])
        self.assertEqual(data['movies']['age'], movies.age)
        movieupdated = Actor.query.get(data['movies']['id'])
        self.assertEqual(movieupdated.id, actor.id)
    def TestDelete_Notfound_Movie(self):
        respo = self.client().delete('/movies/404040')
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertFalse(data['success'])
    def TestUpdate_Notfound_Movie(self):
        updatedData = {
            "title": 'OoOoOoOoOoOo'
        } 
        respo = self.client().update('/movies/update/504030', data=json.dumps(updatedData), headers={'Content-Type': 'application/json'})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertFalse(data['success']) 
    def TestDeleteMovie_ExecutiveProducertoken(self):
        respo = self.client().delete('/movies/1', headers={'Authorization': "Bearer {}".format(self.ExecutiveProducer_token)})
        data = json.loads(respo.data)
        self.assertEqual(respo.status_code, 401)
        self.assertFalse(data["success"])
        self.assertIn('message', data) 

#---------------------------------------------------/
if __name__ == "__main__":
    unittest.main()  


        



























