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
    <html lang=\"pt-BR\">
        <head>
            <meta charset=\"utf-8\" />
            <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
            <title>{settings.app_name}</title>
            <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\" />
            <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin />
            <link href=\"https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&display=swap\" rel=\"stylesheet\" />
            <style>
                :root {{
                    color-scheme: dark;
                    --bg-deep: #020814;
                    --bg-mid: #071829;
                    --text-main: #ecf7ff;
                    --text-soft: #b8cad9;
                    --panel-border: rgba(214, 231, 255, 0.48);
                    --link-bg: rgba(7, 15, 34, 0.75);
                    --link-border: rgba(151, 190, 255, 0.35);
                }}
                * {{ box-sizing: border-box; }}
                body {{
                    margin: 0;
                    min-height: 100vh;
                    font-family: \"Space Grotesk\", \"Avenir Next\", \"Segoe UI\", sans-serif;
                    background:
                        radial-gradient(circle at 20% 10%, rgba(63, 102, 210, 0.26), transparent 35%),
                        radial-gradient(circle at 80% 20%, rgba(69, 183, 255, 0.18), transparent 30%),
                        linear-gradient(180deg, var(--bg-mid), var(--bg-deep));
                    color: var(--text-main);
                    display: grid;
                    place-items: center;
                    padding: 24px;
                }}
                main {{
                    width: min(840px, 100%);
                    border: 1px solid var(--panel-border);
                    border-radius: 24px;
                    background: rgba(255, 255, 255, 0.18);
                    box-shadow:
                        inset 0 1px 0 rgba(255, 255, 255, 0.52),
                        0 24px 70px rgba(0, 0, 0, 0.48);
                    backdrop-filter: blur(18px) saturate(128%);
                    padding: 28px;
                }}
                h1 {{
                    margin: 0;
                    font-size: clamp(2rem, 4vw, 2.8rem);
                    line-height: 1.1;
                    font-weight: 500;
                }}
                p {{ margin: 10px 0; }}
                .subtitle {{ color: var(--text-soft); }}
                .links {{
                    display: flex;
                    flex-wrap: wrap;
                    gap: 10px;
                    margin-top: 14px;
                    margin-bottom: 16px;
                }}
                .doc-link {{
                    border: 1px solid var(--link-border);
                    border-radius: 12px;
                    background: var(--link-bg);
                    color: var(--text-main);
                    cursor: pointer;
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    min-height: 42px;
                    padding: 10px 14px;
                    font-size: 0.92rem;
                    font-weight: 600;
                    text-decoration: none;
                    transition: transform 180ms ease, background 180ms ease, border-color 180ms ease;
                }}
                .doc-link:hover {{
                    transform: translateY(-1px);
                    border-color: rgba(45, 226, 208, 0.95);
                    box-shadow: 0 0 0 2px rgba(45, 226, 208, 0.18);
                }}
                code {{
                    background: rgba(7, 15, 34, 0.8);
                    border: 1px solid rgba(151, 190, 255, 0.25);
                    padding: 2px 8px;
                    border-radius: 8px;
                    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, \"Liberation Mono\", \"Courier New\", monospace;
                }}
            </style>
        </head>
        <body>
            <main>
                <h1>{settings.app_name}</h1>
                <p class=\"subtitle\">Esta e a API publica do Numerus Kovesh.</p>
                <p>Escolha um destino:</p>
                <div class=\"links\">
                    <a class=\"doc-link\" href=\"{settings.frontend_url}\" target=\"_blank\" rel=\"noreferrer\">Frontend</a>
                    <a class=\"doc-link\" href=\"/?doc=openapi\">OpenAPI (Swagger)</a>
                    <a class=\"doc-link\" href=\"/?doc=redoc\">ReDoc</a>
                </div>
                <p>Exemplo de endpoint: <code>POST /v1/numerology</code>.</p>
            </main>
        </body>
    </html>
    """
    return HTMLResponse(content=html)


@app.get("/redoc", include_in_schema=False)
def custom_redoc() -> HTMLResponse:
    html = f"""
    <!doctype html>
    <html lang=\"pt-BR\">
        <head>
            <title>{settings.app_name} - ReDoc</title>
            <meta charset=\"utf-8\"/>
            <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
            <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\" />
            <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin />
            <link href=\"https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600&display=swap\" rel=\"stylesheet\" />
            <style>
                body {{
                    margin: 0;
                    background:
                        radial-gradient(circle at 20% 10%, rgba(63, 102, 210, 0.26), transparent 35%),
                        radial-gradient(circle at 80% 20%, rgba(69, 183, 255, 0.18), transparent 30%),
                        linear-gradient(180deg, #071829, #020814);
                    color: #ecf7ff;
                    font-family: \"Space Grotesk\", \"Avenir Next\", \"Segoe UI\", sans-serif;
                }}
                .fallback {{
                    margin: 12px;
                    padding: 10px 12px;
                    border: 1px solid rgba(151, 190, 255, 0.35);
                    border-radius: 12px;
                    background: rgba(7, 15, 34, 0.75);
                    font-size: 14px;
                }}
                .fallback a {{
                    color: #ecf7ff;
                    font-weight: 600;
                }}
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