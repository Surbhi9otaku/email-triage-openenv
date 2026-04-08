from fastapi import FastAPI
from pydantic import BaseModel

# Try importing your env safely
try:
    from env import EmailEnv
    env = EmailEnv()
except:
    env = None

app = FastAPI()

# Dummy action model (for /step)
class Action(BaseModel):
    response: str = "test"

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/reset")
def reset():
    if env:
        try:
            state = env.reset()
            return {"state": state}
        except Exception as e:
            return {"error": str(e)}
    return {"state": "env not loaded"}

@app.post("/step")
def step(action: Action):
    if env:
        try:
            next_state, reward, done, info = env.step(action)
            return {
                "next_state": next_state,
                "reward": reward,
                "done": done
            }
        except Exception as e:
            return {"error": str(e)}
    return {
        "next_state": "dummy",
        "reward": 0.5,
        "done": False
    }