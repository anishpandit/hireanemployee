from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "HireAnEmployee API is live 🚀"}
