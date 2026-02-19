from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import os
import sys
import shutil
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.core.workspace_assistant import WorkspaceAssistant

app = FastAPI(title="Local AI Workspace Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

assistant = WorkspaceAssistant(data_dir="data")

class SearchQuery(BaseModel):
    query: str

class TaskUpdate(BaseModel):
    task_id: int
    status: str

@app.on_event("startup")
async def startup_event():
    assistant.start()

@app.on_event("shutdown")
async def shutdown_event():
    assistant.stop()

@app.get("/")
async def root():
    return {
        "name": "Local AI Workspace Assistant",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/status")
async def get_status():
    return assistant.get_status()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        upload_dir = "data/uploads"
        os.makedirs(upload_dir, exist_ok=True)
        
        file_path = os.path.join(upload_dir, file.filename)
        
        # Save file
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        print(f"✓ File saved: {file_path}")
        
        # Process file
        assistant.process_file(file_path)
        print(f"✓ File processing started")
        
        return {
            "filename": file.filename,
            "status": "processing",
            "path": file_path
        }
    except Exception as e:
        print(f"✗ Upload error: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/search")
async def search(query: SearchQuery):
    assistant.search(query.query)
    return {"query": query.query, "status": "searching"}

@app.get("/tasks")
async def get_tasks():
    tasks = assistant.get_tasks()
    return {"tasks": tasks, "count": len(tasks)}

@app.get("/memory/recent")
async def get_recent_memory(days: int = 7):
    episodes = assistant.episodic_memory.query_recent(days=days)
    return {"episodes": episodes, "count": len(episodes)}

@app.post("/feedback/correction")
async def record_correction(original: str, corrected: str, correction_type: str):
    assistant.procedural_memory.record_correction(original, corrected, correction_type)
    return {"status": "recorded"}

@app.get("/confirmations")
async def get_confirmations():
    pending = assistant.get_pending_confirmations()
    return {"pending": pending, "count": len(pending)}

@app.post("/confirmations/{item_id}/approve")
async def approve_confirmation(item_id: str, edited_data: dict = None):
    approved = assistant.approve_item(item_id, edited_data)
    return {"status": "approved", "item": approved}

@app.post("/confirmations/{item_id}/reject")
async def reject_confirmation(item_id: str, reason: str = None):
    rejected = assistant.reject_item(item_id, reason)
    return {"status": "rejected", "item": rejected}

@app.get("/ai/status")
async def get_ai_status():
    """Get AI system status"""
    return assistant.get_ai_status()

@app.post("/conflicts/detect")
async def detect_conflicts():
    """Detect conflicts in tasks"""
    assistant.detect_conflicts()
    return {"status": "detecting"}

@app.delete("/tasks/{task_index}")
async def delete_task(task_index: int):
    """Delete a task by index"""
    tasks = assistant.get_tasks()
    if 0 <= task_index < len(tasks):
        deleted = assistant.task_agent.tasks.pop(task_index)
        return {"status": "deleted", "task": deleted}
    raise HTTPException(status_code=404, detail="Task not found")

@app.get("/meetings")
async def get_meetings():
    """Get all processed meetings in structured format"""
    episodes = assistant.episodic_memory.query_recent(days=30, event_type="task")
    return {"meetings": episodes, "count": len(episodes)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
