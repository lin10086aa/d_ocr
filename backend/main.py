"""d_ocr — FastAPI application for PDF OCR to Markdown."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="d_ocr",
    description="PDF 图转文字 — 使用 PP-StructureV3 将 PDF 转为 Markdown",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    """Health check endpoint for CI/CD validation."""
    return {"status": "ok", "service": "d_ocr"}
