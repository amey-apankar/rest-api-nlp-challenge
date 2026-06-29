import logging
import time
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from app.schemas import (
    SummarizeRequest, SummarizeResponse,
    TranslateRequest, TranslateResponse,
    EmailRequest, EmailResponse
)
from app.services import GeminiService

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("api")

gemini_service = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global gemini_service
    gemini_service = GeminiService()
    yield

app = FastAPI(title="IR Infotech REST API Challenge", lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "Welcome to the IR Infotech REST API Challenge", "docs": "/docs"}

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    body = await request.body()
    
    async def receive():
        return {"type": "http.request", "body": body, "more_body": False}
    request._receive = receive

    method = request.method
    path = request.url.path
    logger.info(f"Request: {method} {path} | Body: {body.decode('utf-8', errors='ignore')}")

    try:
        response = await call_next(request)
    except Exception as e:
        logger.error(f"Request failed: {method} {path} | Error: {str(e)}")
        raise e

    process_time = time.time() - start_time
    response_body = b""
    async for chunk in response.body_iterator:
        response_body += chunk
    
    new_response = Response(
        content=response_body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type
    )
    
    logger.info(
        f"Response: {method} {path} | Status: {new_response.status_code} | "
        f"Body: {response_body.decode('utf-8', errors='ignore')} | Time: {process_time:.3f}s"
    )
    return new_response

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred during processing."}
    )

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    logger.error(f"Value error: {str(exc)}")
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)}
    )

@app.post("/summarize", response_model=SummarizeResponse)
async def handle_summarize(payload: SummarizeRequest):
    summary = gemini_service.summarize(payload.text)
    return SummarizeResponse(summary=summary)

@app.post("/translate", response_model=TranslateResponse)
async def handle_translate(payload: TranslateRequest):
    translated = gemini_service.translate(payload.text)
    return TranslateResponse(translated=translated)

@app.post("/generate-email", response_model=EmailResponse)
async def handle_generate_email(payload: EmailRequest):
    email = gemini_service.generate_email(payload.text)
    return EmailResponse(email=email)
