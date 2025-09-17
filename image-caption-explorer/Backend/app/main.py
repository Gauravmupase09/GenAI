# app/main.py
import os
import certifi
import ssl
import urllib3

# Set up SSL configuration
os.environ['SSL_CERT_FILE'] = certifi.where()
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
os.environ['CURL_CA_BUNDLE'] = certifi.where()

# Disable SSL warnings for fallback connections
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Try to configure SSL context
try:
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    ssl_context.check_hostname = True
    ssl_context.verify_mode = ssl.CERT_REQUIRED
except Exception as e:
    print(f"Warning: Could not create SSL context: {e}")

from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Image Caption Explorer",
    description="Upload images, generate captions, fetch similar images, and explore iteratively.",
    version="1.0"
)

# Include the API router with a prefix
app.include_router(router, prefix="/api")

# Simple root endpoint for testing
@app.get("/")
async def root():
    return {"message": "Welcome to Image Caption Explorer!"}