import uvicorn
from fastapi import FastAPI

from src.routes import routes

app = FastAPI()

app.include_router(routes.router, prefix='/api')


@app.get("/")
def read_root():
    return {"message": "GoIT homework #11 - REST API via FastAPI"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 