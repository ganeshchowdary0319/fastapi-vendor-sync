from fastapi import APIRouter
from app.tasks import fetch_and_sync_inventory

sync_router = APIRouter()

@sync_router.post("/sync/")
async def trigger_sync():
    fetch_and_sync_inventory.delay()
    return {"message": "Sync job triggered"}