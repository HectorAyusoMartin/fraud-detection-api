from fastapi import APIRouter
from app.db.session import SessionLocal
from app.models.transaction import Transaction

router = APIRouter(prefix="/transactions",tags=["transactions"])

@router.post("/")
def create_transaction():
    db = SessionLocal()

    transaction = Transaction(
        amount=120.50,
        fraud_probability=0.87,
        prediction="fraud"
    )

    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    db.close()

    return {
        
        "id":transaction.id,
        "amount":transaction.amount,
        "fraud_probability":transaction.fraud_probability,
        "prediction":transaction.prediction,
        "created_at":transaction.created_at,
    }