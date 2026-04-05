from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.record import FinancialRecord


def get_summary(db: Session):
    total_income = db.query(func.sum(FinancialRecord.amount)).filter(
        FinancialRecord.type == "income"
    ).scalar() or 0

    total_expense = db.query(func.sum(FinancialRecord.amount)).filter(
        FinancialRecord.type == "expense"
    ).scalar() or 0

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": total_income - total_expense
    }


def get_category_breakdown(db: Session):
    results = db.query(
        FinancialRecord.category,
        func.sum(FinancialRecord.amount)
    ).group_by(FinancialRecord.category).all()

    return [{"category": r[0], "total": r[1]} for r in results]


def get_recent_activity(db: Session):
    records = db.query(FinancialRecord).order_by(
        FinancialRecord.date.desc()
    ).limit(5).all()

    return records