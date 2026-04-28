from pydantic import BaseModel
from datetime import datetime

class TransactionCreate(BaseModel):
    amount: float
    fraud_probability: float
    prediction: str

class TransactionResponse(BaseModel):

    id:int
    amount:float
    fraud_probability: float
    prediction : str
    created_at: datetime

    class Config:
        from_attributes = True

        

    