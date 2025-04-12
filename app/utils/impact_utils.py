from shapely.geometry import shape
import numpy as np
import pyproj
from shapely.ops import transform
import functools
import math

def calculate_area(geojson_geometry):
    geom = shape(geojson_geometry)

    proj = functools.partial(
        pyproj.transform,
        pyproj.Proj(init="EPSG:4326"),  # WGS84
        pyproj.Proj(init="EPSG:6933")   # Equal-area projection
    )
    
    geom_proj = transform(proj, geom)
    area_sq_m = geom_proj.area
    area_sq_km = area_sq_m / 1_000_000
    
    return area_sq_km


def scaled_biodiversity_loss(area_sq_km):

    factor = np.random.uniform(0.8, 1.2)
    k = 100           
    r = 0.02         
    x0 = 300
    return min(100, k / (1 + math.exp(-r * (area_sq_km - x0))) * factor)


def calculate_environmental_impact(geojson):
    if "geometry" not in geojson:
        raise ValueError("Invalid GeoJSON: missing geometry")
    
    geometry = geojson["geometry"]
    if geometry["type"] not in ("Polygon", "MultiPolygon"):
        raise ValueError("GeoJSON geometry must be Polygon or MultiPolygon")

    area_sq_km = calculate_area(geometry)
    area_sq_km = max(0.01, min(area_sq_km, 5000))  

    biodiversity_loss = scaled_biodiversity_loss(area_sq_km)

    carbon_factor = np.random.uniform(1500, 3000) 
    co2_emission = area_sq_km * carbon_factor

    forest_coverage = np.random.uniform(0.4, 0.9)
    deforested_area = area_sq_km * forest_coverage

    return {
        "biodiversity_loss": round(biodiversity_loss, 2),
        "co2_emission": round(co2_emission, 2),
        "deforested_area": round(deforested_area, 2)
    }
