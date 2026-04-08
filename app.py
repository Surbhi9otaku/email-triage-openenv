@app.post("/reset")
def reset():
    if env:
        try:
            state = env.reset()
            return {"state": state}
        except Exception as e:
            return {"error": str(e)}
    return {"state": "env not loaded"}