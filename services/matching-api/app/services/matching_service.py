import os
from app.models.job import Job
from app.models.matching import MatchingResponse
from app.services.providers.claude import ClaudeProvider

def get_provider():
    provider = os.getenv("AI_PROVIDER", "claude")
    
    if provider == "claude":
        return ClaudeProvider()
    
    raise ValueError(f"Provider '{provider}' not supported yet.")

def match_job_to_resume(job: Job, resume: str) -> MatchingResponse:
    provider = get_provider()
    return provider.match(job, resume)