from fastapi import FastAPI
from uvicorn import run


voting_app = FastAPI()

if __name__ == "__main__":
    run(app=voting_app)
