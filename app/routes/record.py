from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.record import RecordCreate, RecordResponse, RecordUpdate
from app.services.record_service import create_record, get_records, update_record, delete_record

router = APIRouter(prefix="/records", tags=["Records"])


@router.post("/", response_model=RecordResponse)
def create_new_record(record: RecordCreate, db: Session = Depends(get_db)):
    return create_record(db, record)


@router.get("/", response_model=list[RecordResponse])
def get_all_records(
    type: str = Query(None),
    category: str = Query(None),
    db: Session = Depends(get_db)
):
    return get_records(db, type, category)


@router.patch("/{record_id}", response_model=RecordResponse)
def update_existing_record(record_id: int, record: RecordUpdate, db: Session = Depends(get_db)):
    updated = update_record(db, record_id, record)
    if not updated:
        raise HTTPException(status_code=404, detail="Record not found")
    return updated


@router.delete("/{record_id}")
def delete_existing_record(record_id: int, db: Session = Depends(get_db)):
    deleted = delete_record(db, record_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Record not found")
    return {"message": "Record deleted successfully"}