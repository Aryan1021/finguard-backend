from fastapi import FastAPI
from app.database import engine, Base

# Import models (IMPORTANT)
from app.models import user, record

app = FastAPI(title="FinGuard API")

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "FinGuard API Running 🚀"}