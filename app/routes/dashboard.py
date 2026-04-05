from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.dashboard_service import (
    get_summary,
    get_category_breakdown,
    get_recent_activity
)
from app.schemas.record import RecordResponse

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/summary")
def dashboard_summary(db: Session = Depends(get_db)):
    return get_summary(db)


@router.get("/category-breakdown")
def category_breakdown(db: Session = Depends(get_db)):
    return get_category_breakdown(db)


@router.get("/recent", response_model=list[RecordResponse])
def recent_activity(db: Session = Depends(get_db)):
    return get_recent_activity(db)