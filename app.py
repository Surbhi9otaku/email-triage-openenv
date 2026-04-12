from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/reset")
def reset():
    return {"state": "ok"}

@app.post("/step")
def step():
    return {"next_state": "ok", "reward": 0.5, "done": False}