from PIL import Image
import io
import numpy as np
from fastapi import UploadFile
from app.core.model_loader import model

def process_image_to_geojson(image_file: UploadFile):
    image = Image.open(io.BytesIO(image_file.file.read()))
    image_np = np.array(image)

    predictions = model.predict_image(image_np, return_plot=False)

    features = []
    for _, row in predictions.iterrows():
        xmin, ymin, xmax, ymax = row["xmin"], row["ymin"], row["xmax"], row["ymax"]
        score = row.get("score", 1.0)

        feature = {
            "type": "Feature",
            "properties": {"score": score},
            "geometry": {
                "type": "Polygon",
                "coordinates": [[
                    [xmin, ymin],
                    [xmax, ymin],
                    [xmax, ymax],
                    [xmin, ymax],
                    [xmin, ymin]
                ]]
            }
        }
        features.append(feature)

    return {
        "type": "FeatureCollection",
        "features": features
    }
