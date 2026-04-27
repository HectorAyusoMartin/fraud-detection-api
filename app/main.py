from fastapi import FastAPI

from app.api.transactions import router as transactions_router
from app.core.config import settings
from app.db.base import Base
from app.db.session import engine
from app.models.transaction import Transaction


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    description="This is an API for credit card fraud detections",
    version=settings.app_version
)

app.include_router(transactions_router)


@app.get('/')
def root():
    return {'message' : f'{settings.app_name} is running!'}

@app.get('/health')
def health_check():
    return {'status':'ok'}