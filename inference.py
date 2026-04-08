from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "OpenEnv Server is Running"}

# This is the critical part to fix the "POST OK" error
@app.post("/reset")
async def reset():
    # If you have variables to clear, do it here
    return {"status": "success", "message": "Environment reset successfully"}

if __name__ == "__main__":
    # Ensure it runs on port 8000 to match the Dockerfile EXPOSE
    uvicorn.run(app, host="0.0.0.0", port=8000)