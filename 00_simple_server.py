from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# uvicorn 00_simple_server:app --reload --host 0.0.0.0
