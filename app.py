from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Global state
state = {"step": 0}

# Request model
class Action(BaseModel):
    action: str

# Root endpoint (for testing)
@app.get("/")
def home():
    return {"message": "API is running 🚀"}

# Reset environment
@app.post("/reset")
def reset():
    global state
    state = {"step": 0}
    return {
        "message": "reset done",
        "state": state
    }

# Step function
@app.post("/step")
def step(action: Action):
    global state
    state["step"] += 1

    # Simple reward logic
    reward = 1.0 if action.action.lower() == "correct" else 0.0
    done = state["step"] >= 3

    return {
        "state": state,
        "reward": reward,
        "done": done
    }

# Get current state
@app.get("/state")
def get_state():
    return state