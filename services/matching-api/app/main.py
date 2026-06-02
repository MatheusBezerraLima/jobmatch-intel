from fastapi import FastAPI
from app.routes.matching import router as matching_router

app = FastAPI(title="JobMatch Intel - Matching API")

app.include_router(matching_router, prefix="/api/v1")

@app.get("/health")
def health():
    return { "status": "ok"}