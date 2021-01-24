# FSND 
## final project for the Udacity Full Stack Developer Nano Degree.

### Motivation for project
1. I have working with all skills that i have learnt through this valuable course.
In this project, Foucsing on How to write a clean code, Relational Database Architecture, Modeling Data Objects with SQLAlchemy, Developing a Flask API, Authentication and Access, Authentication with Auth0, RBAC, And Deploying Applications.

2. This casting agency project contains three different user roles and related permissions
- Casting Assistant :
  - Can view actors and movies.
- Casting Director :	
  - Can view actors and movies,Add or delete an actor,Modify actors or movies.
- Executive Producer : 
  - Have All permissions.

## Setup Auth0
1. Create an Account Then Select a unique tenant domain after that Create web application
and continue by Creating a new API, The go ahead and chang api settings(Enable RBAC
Enable Add Permissions in the Access Token ).
2. Next step is Creating an API permissions. 
3. third step is to Create roles for our three users.

#### In Postman we can test our endpoints
1. First we have to make sure that we have register our three users and assign each with its own roles.
2. We have to take a valid Token by Sign into each account and make note of the JWT.
3. Run each endpoint individually and do the test. 


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
* note : Token will be invaled after a certain time, So it must be refreshed. 
For testing the backend, run the following commands :
```bash
source setup.sh
python test.py
```

## Access project in Heroku URL:
( https://afrafsnd.herokuapp.com/ )

## Access project locally:
( http://127.0.0.1:5000/ )


