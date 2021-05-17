from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return {"Localization": "Internet Protocol"}


if __name__ == '__main__':
    app.run()
