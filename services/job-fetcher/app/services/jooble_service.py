import httpx
import os 
from app.models.job import JoobleJob

JOOBLE_API_KEY = os.getenv("JOOBLE_API_KEY")
JOOBLE_URL = f"https://jooble.org/api/{JOOBLE_API_KEY}"

async def fetch_jobs(title: str, location: str) -> list[JoobleJob]:
    payload = {
        "keywords": title,
        "location": location
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(JOOBLE_URL, json=payload)
        response.raise_for_status()
        data = response.json()

    print("JOOBLE RESPONSE:", data)  # log temporário

    jobs = []
    for item in data.get("jobs", []):
        jobs.append(JoobleJob(
            title=item.get("title", ""),
            company=item.get("company", ""),
            location=item.get("location", ""),
            description=item.get("snippet", ""),
            link=item.get("link", ""),
            salary=item.get("salary"),
            updated=item.get("updated")
        ))
    
    if not jobs:
        return get_mock_jobs()
    
    return jobs


def get_mock_jobs() -> list[JoobleJob]:
    return [
        JoobleJob(
            title="Desenvolvedor Backend Python",
            company="TechCorp Brasil",
            location="São Paulo, SP",
            description="Vaga para desenvolvedor backend com experiência em Python, FastAPI, PostgreSQL e Docker. Desejável conhecimento em AWS e automação.",
            link="https://exemplo.com/vaga/1",
            salary="R$ 8.000 - R$ 12.000",
            updated="2026-06-01"
        ),
        JoobleJob(
            title="Engenheiro de Software Backend",
            company="Startup Inovação",
            location="Remoto",
            description="Buscamos desenvolvedor backend com foco em Node.js ou Python, experiência com APIs REST, bancos relacionais e ferramentas de automação.",
            link="https://exemplo.com/vaga/2",
            salary="R$ 10.000 - R$ 15.000",
            updated="2026-06-02"
        )
    ]