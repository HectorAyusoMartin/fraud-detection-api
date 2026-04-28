from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionResponse
from app.core.security import get_current_user

router = APIRouter(prefix="/transactions",tags=["transactions"], dependencies=[Depends(get_current_user)])

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

@router.get("/", response_model=list[TransactionResponse])
def get_transactions(db:Session = Depends(get_db)):
    return db.query(Transaction).all()

@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction_by_id(transaction_id: int, db : Session = Depends(get_db)):

    transaction = db.get(Transaction, transaction_id)

    if transaction is None:
        raise HTTPException(
            status_code=404,
            detail="Transaction not found"
        )
    return transaction

@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, db : Session = Depends(get_db)):
    transaction = db.get(Transaction, transaction_id)

    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    db.delete(transaction)
    db.commit()

    return {"message":"Transaction deleted sucessfully"}
                       