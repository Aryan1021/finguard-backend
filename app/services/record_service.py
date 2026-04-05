from sqlalchemy.orm import Session
from app.models.record import FinancialRecord
from app.schemas.record import RecordCreate, RecordUpdate


def create_record(db: Session, record: RecordCreate):
    db_record = FinancialRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


def get_records(db: Session, type=None, category=None):
    query = db.query(FinancialRecord)

    if type:
        query = query.filter(FinancialRecord.type == type)

    if category:
        query = query.filter(FinancialRecord.category == category)

    return query.all()


def update_record(db: Session, record_id: int, data: RecordUpdate):
    record = db.query(FinancialRecord).filter(FinancialRecord.id == record_id).first()
    
    if not record:
        return None

    for key, value in data.dict(exclude_unset=True).items():
        setattr(record, key, value)

    db.commit()
    db.refresh(record)
    return record


def delete_record(db: Session, record_id: int):
    record = db.query(FinancialRecord).filter(FinancialRecord.id == record_id).first()

    if not record:
        return None

    db.delete(record)
    db.commit()
    return record