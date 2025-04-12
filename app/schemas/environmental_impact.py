from pydantic import BaseModel 

class EnvironmentalImpact(BaseModel): 
    zone_id: str
    biodiversity_loss: float  
    co2_emission: float    
    deforested_area: float
