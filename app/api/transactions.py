from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.transaction import Transaction

router = APIRouter(prefix="/transactions",tags=["transactions"])

@router.post("/")
def create_transaction(db: Session = Depends(get_db)):
    
    transaction = Transaction(
        amount=120.50,
        fraud_probability=0.87,
        prediction="fraud"
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return {
        
        "id":transaction.id,
        "amount":transaction.amount,
        "fraud_probability":transaction.fraud_probability,
        "prediction":transaction.prediction,
        "created_at":transaction.created_at,
    }