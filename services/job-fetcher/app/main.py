from fastapi import FastAPI
from app.routes.jobs import router as jobs_router

app = FastAPI(title="JobMatch Intel - Job Fetcher")

app.include_router(jobs_router, prefix="/api/v1")

@app.get("/health")
def health():
    return {"status": "ok"}