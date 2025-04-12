from pydantic import BaseModel
from typing import List, Optional, Union

class Geometry(BaseModel):
    type: str
    coordinates: Union[List, List[List], List[List[List]]]

class FeatureProperties(BaseModel):
    score: Optional[float] = None

class Feature(BaseModel):
    type: str = "Feature"
    properties: FeatureProperties
    geometry: Geometry

class FeatureCollection(BaseModel):
    type: str = "FeatureCollection"
    features: List[Feature]
