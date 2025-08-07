# Vendor Inventory Sync API

This FastAPI-based microservice asynchronously fetches inventory data from an external vendor API and syncs it to the internal system using Celery and Redis.

## Features

- FastAPI for API interface
- Celery for background task execution
- Redis as message broker
- HTTPX for async HTTP requests

## Setup Instructions

1. Clone the repo
2. Create a virtual environment and activate it
3. Install dependencies: `pip install -r requirements.txt`
4. Start Redis locally (or use Docker)
5. Run the FastAPI app: `uvicorn app.main:app --reload`
6. Start the Celery worker: `celery -A app.tasks.celery_app worker --loglevel=info`

## API Endpoint

`POST /sync/` - Triggers the background inventory sync task

## Author

Ganesh — Python Backend Engineer