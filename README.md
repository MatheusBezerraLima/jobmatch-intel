# JobMatch Intel

> Stop scrolling job boards. Let AI find the opportunities that actually fit you.

**JobMatch Intel** is an automated job matching pipeline that continuously scans job listings, scores them against your résumé using Claude AI, identifies skill gaps, and delivers ranked opportunities directly to your inbox — all running locally on Docker.

Built for developers who are serious about their job search and their own growth.

---

## ✨ Features

- 🤖 **AI-powered matching** — Claude analyzes each vacancy against your résumé and returns a compatibility score with detailed justification
- 📊 **Ranked opportunities** — vacancies sorted by fit score so you focus on what matters
- 🧩 **Gap analysis** — understand exactly why you don't fit a role and what to learn next
- 📬 **Automated alerts** — get notified when a high-score opportunity appears
- 📈 **Weekly reports** — track how your profile evolves over time
- 🔧 **Fully configurable** — swap your résumé, target role, location, and job sources in minutes

---

## 🛠️ Stack

| Layer | Technology |
|---|---|
| Orchestration | [n8n](https://n8n.io/) |
| Matching API | [FastAPI](https://fastapi.tiangolo.com/) + Python 3.11 |
| AI Engine | Configurable via AI_PROVIDER | default: [Claude API](https://www.anthropic.com/) (Anthropic) |
| Database | PostgreSQL 15 |
| Cache & Queues | Redis 7 |
| Infrastructure | Docker + Docker Compose |

---

## 🏗️ Architecture

```
[Job APIs] ──► [n8n Orchestrator] ──► [matching-api (FastAPI)]
                      │                        │
                      │                   [Claude API]
                      │                        │
                      ▼                        ▼
               [n8n Workflows]          [PostgreSQL]
               [Email Alerts]           [Redis Cache]
```

**How it works:**
1. n8n triggers a scheduled workflow (daily or on-demand)
2. Fetches job listings from the configured Job API
3. Sends each vacancy + your résumé to the matching-api
4. matching-api calls Claude, which scores the match and identifies gaps
5. Results are saved to PostgreSQL and delivered to your inbox

---

## 📁 Project Structure

```
jobmatch-intel/
├── docs/                          # Architecture docs and diagrams
├── infra/
│   ├── docker-compose.yml         # All services orchestrated
│   └── .env.example               # Environment variables template
├── services/
│   ├── matching-api/              # FastAPI microservice
│   │   ├── app/
│   │   │   ├── main.py
│   │   │   ├── routes/            # API endpoints
│   │   │   ├── models/            # Pydantic DTOs
│   │   │   └── services/          # Business logic
│   │   │       └── providers/          # Define supported AI engine models.
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   └── n8n/
│       └── workflows/             # Exported n8n workflows (ready to import)
├── scripts/
│   └── setup.sh                   # One-command setup helper
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) and Docker Compose installed
- An [Anthropic API key](https://console.anthropic.com/) (Claude)
- An account on a supported Job API (see [Supported Sources](#supported-job-sources))

### 1. Clone the repository

```bash
git clone https://github.com/MatheusBezerraLima/jobmatch-intel.git
cd jobmatch-intel
```

### 2. Configure environment variables

```bash
cp infra/.env.example infra/.env
```

Open `infra/.env` and fill in your credentials:

```env
POSTGRES_USER=jobmatch
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=jobmatch_db
ANTHROPIC_API_KEY=your_anthropic_api_key
JOB_API_KEY=your_job_api_key

AI_PROVIDER=claude
```

 `` - The AI ​​provider can be changed in the IA_PROVIDER field (ex: Ollama).``

### 3. Add your resume

Open `services/matching-api/app/resume.txt` and paste your résumé in plain text. The more detail, the better the matching.

### 4. Start all services

```bash
cd infra
docker compose up -d
```

### 5. Import the n8n workflow

1. Open [http://localhost:5678](http://localhost:5678)
2. Go to **Workflows → Import**
3. Import the file at `services/n8n/workflows/job-matching-mvp.json`
4. Activate the workflow

### 6. Verify the API

```bash
curl http://localhost:8000/health
# {"status": "ok"}
```

Full API docs available at [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🌐 Supported Job Sources

| Source | Region | Free Tier |
|---|---|---|
| [Jooble](https://jooble.org/api/about) | Brazil 🇧🇷 | ✅ Yes |
| [Adzuna](https://developer.adzuna.com/) | Brazil 🇧🇷 + International 🌍 | ✅ Yes |

> International sources coming in v2.

---

## 🗺️ Roadmap

### v1 — MVP (current)
- [x] Docker Compose infrastructure
- [x] FastAPI matching microservice
- [x] Claude AI integration
- [x] n8n base workflow
- [ ] Job API integration (Jooble)
- [ ] Email alerts for high-score matches
- [ ] PostgreSQL persistence layer

### v2 — Expansion
- [ ] Vacancy ranking dashboard (React + Leaflet)
- [ ] Weekly skill gap reports
- [ ] International job sources
- [ ] WhatsApp alerts via n8n

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/your-username/jobmatch-intel.git

# 3. Create a feature branch
git checkout -b feat/your-feature-name

# 4. Make your changes and commit
git commit -m "feat: describe your change"

# 5. Push and open a Pull Request
git push origin feat/your-feature-name
```

Please follow the [Conventional Commits](https://www.conventionalcommits.org/) standard for commit messages.

---

## 📄 License

MIT License — feel free to use, modify and distribute.

---

<p align="center">Built with ⚙️ n8n + 🐍 FastAPI + 🤖 AI Engine + </p>