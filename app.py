from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Action(BaseModel):
    action: str = "test"

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    return {
        "state": {
            "email": "sample email",
            "category": "general"
        }
    }

@app.post("/step")
def step(action: Action):
    return {
        "next_state": {
            "email": "processed email"
        },
        "reward": 0.5,
        "done": False
    }