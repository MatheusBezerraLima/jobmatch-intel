from fastapi import APIRouter 
from app.models.matching import MatchingRequest, MatchingResponse
from app.services.matching_service import match_job_to_resume

router = APIRouter()

@router.post("/match", response_model=MatchingResponse)
def match(request: MatchingRequest):
    return match_job_to_resume(request.job, request.resume)

