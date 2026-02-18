"""
File ingestion endpoints.
Handles uploading and processing documents.
"""
from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List

router = APIRouter()

@router.post("/files")
async def upload_files(files: List[UploadFile] = File(...)):
    """
    Upload and ingest files (PDF, DOCX, XLSX, TXT).
    Files are processed locally and stored in the encrypted vault.
    """
    # TODO: Implement file ingestion
    return {"message": "File ingestion endpoint - coming soon", "files": [f.filename for f in files]}

@router.post("/text")
async def ingest_text(text: str):
    """
    Manually ingest text content.
    """
    # TODO: Implement text ingestion
    return {"message": "Text ingestion endpoint - coming soon", "text_length": len(text)}

