from fastapi import FastAPI
from slate.backend.src.api import narratives

app = FastAPI()

app.include_router(narratives.app, prefix="/api", tags=["narratives"])


@app.get("/")
def read_root():
    return {"message": "Welcome to Slate's Words for Tomorrow API!"}
