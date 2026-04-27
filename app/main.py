from fastapi import FastAPI

app = FastAPI(
    title="Fraud Detection API",
    description="This is an API for credit card fraud detections"
)


@app.get('/')
def root():
    return {'message' : 'launch!'}

@app.get('/health')
def health_check():
    return {'status':'ok'}