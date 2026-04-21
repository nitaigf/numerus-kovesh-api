from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse

from app.api.routes.health import router as health_router
from app.api.routes.numerology import router as numerology_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Public numerology API: normalization, mapping, reduction and meanings.",
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
def root_redirect(doc: str | None = None):
    if doc:
        requested_doc = doc.lower()
        if requested_doc == "redoc":
            return RedirectResponse(url="/redoc")
        if requested_doc == "openapi":
            return RedirectResponse(url="/docs")

    html = f"""
    <!doctype html>
    <html lang=\"en\">
        <head>
            <meta charset=\"utf-8\" />
            <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
            <title>{settings.app_name}</title>
            <style>
                body {{
                    margin: 0;
                    background: #07121f;
                    color: #ecf5ff;
                    font-family: Georgia, 'Times New Roman', serif;
                    display: grid;
                    place-items: center;
                    min-height: 100vh;
                    padding: 24px;
                }}
                main {{
                    width: min(760px, 100%);
                    border: 1px solid rgba(127, 181, 255, 0.28);
                    border-radius: 18px;
                    background: linear-gradient(180deg, rgba(9, 22, 38, 0.92), rgba(7, 13, 25, 0.96));
                    box-shadow: 0 24px 90px rgba(0, 0, 0, 0.45);
                    padding: 24px;
                }}
                h1 {{ margin-top: 0; }}
                a {{ color: #92d2ff; }}
                ul {{ line-height: 1.8; }}
                code {{ background: #0c1830; padding: 2px 6px; border-radius: 6px; }}
            </style>
        </head>
        <body>
            <main>
                <h1>{settings.app_name}</h1>
                <p>Esta e a API publica do Numerus Kovesh.</p>
                <p>Escolha um destino:</p>
                <ul>
                    <li>Frontend: <a href=\"{settings.frontend_url}\" target=\"_blank\" rel=\"noreferrer\">{settings.frontend_url}</a></li>
                    <li>OpenAPI (Swagger): <a href=\"/?doc=openapi\">/?doc=openapi</a></li>
                    <li>ReDoc: <a href=\"/?doc=redoc\">/?doc=redoc</a></li>
                </ul>
                <p>Exemplo: <code>POST /v1/numerology</code>.</p>
            </main>
        </body>
    </html>
    """
    return HTMLResponse(content=html)


@app.get("/redoc", include_in_schema=False)
def custom_redoc() -> HTMLResponse:
    html = f"""
    <!doctype html>
    <html>
        <head>
            <title>{settings.app_name} - ReDoc</title>
            <meta charset=\"utf-8\"/>
            <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
            <style>
                body {{ margin: 0; background: #07121f; color: #ecf5ff; font-family: Georgia, 'Times New Roman', serif; }}
                .fallback {{
                    margin: 12px;
                    padding: 10px 12px;
                    border: 1px solid rgba(127, 181, 255, 0.28);
                    border-radius: 10px;
                    background: rgba(9, 22, 38, 0.92);
                    font-size: 14px;
                }}
                .fallback a {{ color: #92d2ff; }}
            </style>
        </head>
        <body>
            <div class=\"fallback\">Caso esta documentacao nao carregue no seu ambiente, use <a href=\"/docs\">/docs</a>.</div>
            <redoc spec-url=\"/openapi.json\"></redoc>
            <script src=\"https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js\"></script>
        </body>
    </html>
    """
    return HTMLResponse(content=html)


app.include_router(health_router)
app.include_router(numerology_router)