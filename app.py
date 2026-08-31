from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to Castaway Cinema - India",
        "status": "Application not  running",
        "version": "0.1"
    }

@app.get("/movies")
def movies():
    return {
        "movies": [
            "Cast",
            "stellar",
            "Ince",
            "Lovely nes",
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
@app.get("/version")
def version():
    return {
        "message": "Welcome to Castaway Cinema",
        "status": "Application is running",
        "version": "1.1"
    }