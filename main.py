from fastapi import FastAPI
from app.geoloc.services import Service

app = FastAPI()


@app.get('/')
async def root():
    return {"Localization": "Internet Protocol"}


@app.post('/locateip')
async def locIP(ip):
    res = Service()
    loc = res.get_geoloc(ip)

    return loc


if __name__ == '__main__':
    app.run()
