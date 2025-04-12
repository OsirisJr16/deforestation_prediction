from fastapi import APIRouter, Body, UploadFile, File
from app.utils.image_utils import process_image_to_geojson
from app.schemas.prediction import FeatureCollection
from app.schemas.environmental_impact import EnvironmentalImpact 
from app.utils.impact_utils import calculate_environmental_impact 

router = APIRouter(prefix="/api")

@router.post("/predict", response_model=FeatureCollection)
async def predict(image: UploadFile = File(...)):
    geojson_result = process_image_to_geojson(image)
    return geojson_result

@router.post("/impact", response_model=EnvironmentalImpact)
def get_environmental_impact(geojson: dict = Body(...)):
    impact_data = calculate_environmental_impact(geojson)
    return {
        "zone_id": geojson.get("id", "unknown"),
        **impact_data
    }