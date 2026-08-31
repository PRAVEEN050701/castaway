from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to Castaway Cinema",
        "status": "Application is running"
    }

@app.get("/movies")
def movies():
    return {
        "movies": [
            "Castaway",
            "Interstellar",
            "Inception",
            "Lovely Bones",
            "Light House",
            "Dune",
            "Oppenheimer"
        ]
    }
@app.get("/about")
def about():
    return {
        "name": "Castaway Cinema",
        "location": "Chennai",
        "type": "Cinema Management System"
    }
