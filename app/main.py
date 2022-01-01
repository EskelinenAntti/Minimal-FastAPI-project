import logging

from fastapi import FastAPI

from app.routers import notes
from app import db

# Setup logging. Without this line logs are not printed to terminal when using uvicorn.
logging.basicConfig(level=logging.INFO)

# Create database tables on app startup. Note that this should not be used in a production setting.
db.create_tables()

app = FastAPI()
app.include_router(notes.router, prefix="/notes")


