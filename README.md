# FSND :
The Capstone project is about Casting Agency that supports a basic casting agency by allowing users to query the database for movies and actors.

## final project for the Udacity Full Stack Developer Nano Degree.
 This casting agency project contains three different user roles and related permissions	
- Casting Assistant: Can view actors and movies
- Casting Director:	Can view actors and movies,Add or delete an actor,Modify actors or movies
- Executive Producer: Have All permissions

## Installation
### python 3.8
Follow instructions to install the latest version of python for your platform in the [python docs] (https://docs.python.org/3/using/index.html)

### Virtual Enviornment 
Recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized.

### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by running:
```bash
pip install -r requirements.txt
```

### Running the server
From within the root directory, first ensure you're working with your created
venv. To run the server, execute the following:
```bash
export FLASK_APP=app.py
export FLASK_DEBUG=true
export FLASK_ENV=development
flask run
```
Or you can use 
```bash
python -m flask run 
```
instead of flask run if you faced any problems.

## Endpoins:
- GET /actors and /movies
http://127.0.0.1:5000/actors 
```json
{
    "actors": [
        {
            "gender": "female",
            "id": 4,
            "movieid": 1,
            "name": "sara"
        },
        {
            "gender": "female",
            "id": 5,
            "movieid": 1,
            "name": "sareeea"
        }
    ],
    "success": true
}
```
http://127.0.0.1:5000/movies
```json
{
    "movies": [
        {
            "id": 1,
            "releasedate": "Wed, 13 Jan 2021 00:00:00 GMT",
            "title": "aa"
        },
        {
            "id": 2,
            "releasedate": "Sat, 13 Jan 2091 00:00:00 GMT",
            "title": "aalkmn"
        },
        {
            "id": 3,
            "releasedate": "Sat, 13 Jan 2091 00:00:00 GMT",
            "title": "aalkmn"
        }
    ],
    "success": true
}
```
- DELETE /actors/ and /movies
http://127.0.0.1:5000/actors/4
```json
{
    "actor_id": 4,
    "message": "Actor info has been Deleted successfully",
    "success": true
}
```
http://127.0.0.1:5000/movies/2
```
{
    "message": "Movie info has been Deleted successfully",
    "movie_id": 2,
    "success": true
}
```
- POST /actors and /movies
http://127.0.0.1:5000/actors/create
```json
{
    "created": 7,
    "message": "New Actor has been created successfully",
    "newactor": {
        "gender": "female",
        "id": 7,
        "movieid": 1,
        "name": "lolla"
    },
    "success": true
}
```
http://127.0.0.1:5000/movies/create
```json
{
    "created": 4,
    "message": "New Movie has been created successfully",
    "newmovie": {
        "id": 4,
        "releasedate": "Mon, 13 Jan 2025 00:00:00 GMT",
        "title": "peewooo"
    },
    "success": true
}
```
- PATCH /actors/ and /movies
http://127.0.0.1:5000/actors/update/7
```json
{
    "message": "Actor info has been Updated successfully",
    "success": true
}
```
http://127.0.0.1:5000/movies/patch/3
```json
{
    "message": "Movie info has been Updated successfully",
    "success": true
}
```
#ErrorHandling:
________________
- 401
```json
{
	"success": False,
	"error": 401,
	"message": "Authentication Error."
}
________________
- 404
{
	"success": False,
    "error": 404,
    "message": "Not found."
}
________________
- 422
{
	"success": False,
    "error": 422,
    "message": "Request could not be processed."
}
________________
```
## Testing
For testing the backend, run the following commands :

dropdb capstone
createdb capstone
psql capstone < casting.sql
python test.py

## Access project in Heroku URL:
( https://afrafsnd.herokuapp.com/ )

## Access project locally:
( http://127.0.0.1:5000/ )


