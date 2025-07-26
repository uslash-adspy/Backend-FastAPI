import sys
sys.path.append("./app/")
from fastapi import FastAPI
from schemas import ResetResponse
from routers import chat, playlist, user
from services import ChatService, PlaylistService, UserService

app = FastAPI(title="2025 SSF Para Backend", version="1.0.0")

chat_service = ChatService()
playlist_service = PlaylistService()
user_service = UserService()

app.include_router(chat.router)
app.include_router(playlist.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Para in 2025 SSF"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
