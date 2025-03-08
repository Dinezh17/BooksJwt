from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def defaultget():
    return {
        "hello":"World this is the root api"
    }