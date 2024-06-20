from fastapi import FastAPI

from dotenv import load_dotenv
import os
app = FastAPI()


@app.get("/")
def read_root():
    load_dotenv(".env")
    ENVIRONMENT = os.environ.get("ENVIRONMENT")
    return {"Hello": f"World from ENVIRONMENT={ENVIRONMENT}"}
