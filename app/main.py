from fastapi import FastAPI
from app.routes import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Deforestation Predictor API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)