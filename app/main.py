from fastapi import FastAPI
from app.sync import sync_router

app = FastAPI(title="Vendor Sync Service")
app.include_router(sync_router)