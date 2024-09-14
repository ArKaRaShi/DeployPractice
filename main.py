from fastapi import FastAPI
import nest_asyncio
import uvicorn

app = FastAPI()

@app.get("/")
async def main():
    return {"Lucky": "Hello"}

@app.get("/lucky")
async def getLucky():
    return {"WWWWWWWWWW": "ARRRRRRR"}


nest_asyncio.apply()
uvicorn.run(app, host="0.0.0.0", port=8000)