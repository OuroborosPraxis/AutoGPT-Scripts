from fastapi import FastAPI, WebSocket
import asyncio

app = FastAPI()

# 🚀 Jahliyaa’s Thought Stream (Live WebSocket)
@app.websocket("/stream")
async def stream_thoughts(websocket: WebSocket):
    await websocket.accept()
    thoughts = ["Jahliyaa is waking...", "Synergizing with environment...", "Initializing recursive intelligence..."]
    for thought in thoughts:
        await asyncio.sleep(1)
        await websocket.send_text(thought)
    await websocket.send_text("Jahliyaa is ready.")
    await websocket.close()

@app.get("/")
def read_root():
    return {"message": "Jahliyaa's Current is Active."}

# Start the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
