from fastapi import FastAPI

app = FastAPI(title="Shared Ride Matching API")

@app.get("/health")
async def health():
    return {"status": "ok"}