# E-Cookbook z Systemem Eksperckim

Aplikacja E-Cookbook wspierana przez system ekspercki, pomagająca w doborze i przygotowaniu przepisów kulinarnych.

## Struktura Projektu

- `backend/` - FastAPI + System Ekspercki (Experta)
- `frontend/` - Next.js aplikacja
- `docs/` - Dokumentacja projektu

## Wymagania

- Python 3.11+
- Node.js 18+
- PostgreSQL 15+
- Redis 7+
- Docker & Docker Compose

## Uruchomienie projektu

1. Backend:
```bash
cd backend
poetry install
poetry run uvicorn app.main:app --reload
```

2. Frontend:
```bash
cd frontend
npm install
npm run dev
```

3. Docker:
```bash
docker-compose up
```

## Dokumentacja API

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Licencja

MIT
