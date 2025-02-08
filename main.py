from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hallo": "Mandarine"}

@app.get("/stachel")
def read_stachel():
    return {"Pico": "Der Stachel der Klarheit ist da!"}
