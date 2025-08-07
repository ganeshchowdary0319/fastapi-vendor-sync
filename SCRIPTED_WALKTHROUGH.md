# Scripted Walkthrough for Interview

## Project Name: Vendor Inventory Sync API

### 1. Purpose
This microservice fetches product inventory data from an external vendor API and syncs it into our internal systems. It's built to be scalable, async, and fault-tolerant.

### 2. Architecture & Tech Stack
- FastAPI for the API endpoint
- Celery + Redis for background job queue
- HTTPX for making async HTTP requests
- Docker for containerization

### 3. Demo Flow
- Run `POST /sync/` endpoint from Postman or Swagger UI.
- This enqueues a background task in Celery to pull inventory from an external API (mocked).
- The task logs the result and shows successful integration.

### 4. Challenges and Resolutions
- Challenge: Ensuring async task processing with high volume.
- Solved with: Celery’s reliability and Redis’s speed as broker.

### 5. Result
This setup ensures our systems stay in sync with minimal latency and can scale independently of the request lifecycle.