from pydantic import BaseModel

class TransactionCreate(BaseModel):
    amount: float
    fraud_probability: float
    prediction: str
    