# Numerus Kovesh API

API publica de numerologia pitagorica do ecossistema Numerus Kovesh.

## Stack

- FastAPI
- Pydantic v2
- pytest
- Deploy serverless na Vercel

## Estrutura

```text
.
├── api/
│   ├── app/
│   ├── tests/
│   ├── index.py
│   ├── requirements.txt
│   └── vercel.json
├── bruno/
├── .github/workflows/
├── Makefile
└── README.md
```

## Executar localmente

```bash
cd api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
cp .env.example .env
python3 -m app.run
```

API local: http://localhost:8010

## Testes

```bash
make test
```

## Endpoint principal

```http
POST /v1/numerology
Content-Type: application/json

{
	"text": "Nitai Embras"
}
```

Resposta de sucesso:

```json
{
	"input": "Nitai Embras",
	"normalized": "NITAIEMBRAS",
	"letters": [
		{ "char": "N", "value": 5 },
		{ "char": "I", "value": 9 }
	],
	"sum": 52,
	"reduced": 7,
	"is_master": false,
	"meaning": "Espiritualidade"
}
```

## Deploy

Na Vercel, usar Root Directory = `api`.

## Contrato

O contrato HTTP compartilhado entre Web e API deve viver no repositorio pai.
