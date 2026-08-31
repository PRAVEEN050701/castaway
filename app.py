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
    
