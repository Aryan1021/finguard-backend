from fastapi import FastAPI
from app.database import engine, Base
from app.models import user, record
from app.routes import user

app = FastAPI(title="FinGuard API")

Base.metadata.create_all(bind=engine)

app.include_router(user.router)

@app.get("/")
def home():
    return {"message": "FinGuard API Running 🚀"}