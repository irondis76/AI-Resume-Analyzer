from __future__ import annotations

from fastapi import APIRouter, File, HTTPException, UploadFile

from ...core.config import settings
from ...core.parser import parse_resume
from ...core.models import AnalysisResult
from ...ai.workflow import build_graph


router = APIRouter()
graph = build_graph()


@router.post("/analyze", response_model=AnalysisResult)
async def analyze(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".pdf", ".docx")):
        raise HTTPException(status_code=400, detail="Only PDF and DOCX files are supported")

    content = await file.read()
    max_bytes = settings.upload_max_mb * 1024 * 1024
    if len(content) > max_bytes:
        raise HTTPException(status_code=413, detail=f"File too large. Max {settings.upload_max_mb}MB")

    resume = parse_resume(content, filename=file.filename)
    result = graph.invoke({"resume": resume})
    return result["result"]


