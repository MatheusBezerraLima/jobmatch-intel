from fastapi import APIRouter
from app.services.jooble_service import fetch_jobs
from app.models.job import JoobleJob

router = APIRouter()

@router.get("/jobs", response_model=list[JoobleJob])
async def get_jobs(title: str, location: str = "Brasil"):
    return await fetch_jobs(title, location)