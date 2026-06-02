from app.models.job import Job
from app.models.matching import MatchingResponse

def match_job_to_resume(job: Job, resume: str) -> MatchingResponse:
    return MatchingResponse(
        score=85,
        justification= "O candidato possui experiência sólida com as tecnologias requeridas.",
        gaps=["Kubernetes", "AWS Certified"],
        recommendations=[
            "Adicionar projetos com Kubernetes ao portfólio",
            "Considerar certificação AWS Developer"
        ]
    )