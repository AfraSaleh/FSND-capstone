#final project for the Udacity Full Stack Developer Nano Degree.

#Endpoins:
- GET /actors and /movies
- DELETE /actors/ and /movies
- POST /actors and /movies
- PATCH /actors/ and /movies

#ErrorHandling:
________________
- 401
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

