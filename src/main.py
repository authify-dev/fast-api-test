from fastapi import FastAPI

from core.settings import settings

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": f"World from ENVIRONMENT={settings.ENVIRONMENT}"}
