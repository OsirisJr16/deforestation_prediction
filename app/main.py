from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Deforestation Predictor API")
app.include_router(router)