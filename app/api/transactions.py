from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate

router = APIRouter(prefix="/transactions",tags=["transactions"])

@router.post("/")
def create_transaction(payload: TransactionCreate ,db: Session = Depends(get_db)):
    
    transaction = Transaction(
        amount=payload.amount,
        fraud_probability=payload.fraud_probability,
        prediction=payload.prediction,
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