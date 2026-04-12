from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}


# REQUIRED by OpenEnv validator
def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()