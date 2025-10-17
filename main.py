from fastapi import FastAPI, Request, HTTPException

app = FastAPI()

SECRET = "saundhariya_iyer"

@app.post("/api-endpoint")
async def receive_task(request: Request):
    data = await request.json()

    if data.get("secret") != SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    return {
        "status": "OK",
        "message": "Task received successfully",
        "email": data.get("email"),
        "task": data.get("task"),
        "round": data.get("round")
    }
