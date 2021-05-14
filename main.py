import uvicorn
from fastapi import FastAPI
from app.router import apiRouter

app = FastAPI()
app.include_router(apiRouter, prefix='/v1')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
