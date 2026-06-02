from app.models.job import Job
from app.models.matching import MatchingResponse
from app.services.providers.base import BaseAIProvider

class ClaudeProvider(BaseAIProvider):

    def match(self, job: Job, resume: str) -> MatchingResponse:
        # TODO: substituir pelo Claude real quando tiver ANTHROPIC_API_KEY
        return MatchingResponse(
            score=85,
            justification="O candidato possui experiência sólida com as tecnologias requeridas.",
            gaps=["Kubernetes", "AWS Certified"],
            recommendations=[
                "Adicionar projetos com Kubernetes ao portfólio",
                "Considerar certificação AWS Developer"
            ]
        )