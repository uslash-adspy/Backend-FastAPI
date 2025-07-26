import sys
sys.path.append("./app/")
from fastapi import FastAPI
from routers import chat, analyze

app = FastAPI(title="Backend-FastAPI", version="1.0.0")


app.include_router(chat.router)
app.include_router(analyze.router)

@app.get("/")
async def root():
    return {"message": ""}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)
