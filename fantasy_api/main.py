import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

def start():
    uvicorn.run("fantasy_api.main:app", host="0.0.0.0", reload=True, port=8000)