from celery import Celery
import httpx

celery_app = Celery("worker", broker="redis://localhost:6379/0")

@celery_app.task
def fetch_and_sync_inventory():
    vendor_url = "https://api.vendor.com/inventory"
    response = httpx.get(vendor_url)
    if response.status_code == 200:
        inventory = response.json()
        print("Inventory fetched and ready to sync:", inventory)