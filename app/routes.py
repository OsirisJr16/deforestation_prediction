from fastapi import APIRouter, UploadFile, File
from app.utils.image_utils import process_image_to_geojson
from app.schemas.prediction import FeatureCollection

router = APIRouter(prefix="/api")

@router.post("/predict", response_model=FeatureCollection)
async def predict(image: UploadFile = File(...)):
    geojson_result = process_image_to_geojson(image)
    return geojson_result
