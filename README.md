# digipower


Digital power project

Contents:
	Web (./src) - FastAPI server for requests
	
	Avatar (./avatar) - FastAPI server instance 2, with a program to create an avatar
	
	
	
	
	
Database contents (do note that passwords are stored in hashed form in the db itself):

{
    "kwaffle": {
        "username": "kwaffle",
        "password": "qwerty123"
    },
    "moloko_horol": {
        "username": "moloko_horol",
        "password": "passwordpassword"
    },
    "spidermind": {
            "username": "spidermind",
            "password": "lolkekcheburek"
        },
}
	
	
	
To start docker-compose and get both of container up and running:
docker-compose up -d --build


To run tests after that:
docker-compose exec web pytest
	