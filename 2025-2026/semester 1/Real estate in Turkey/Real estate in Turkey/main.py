from classes import DataRequest
import pandas as pd
import fastapi
import joblib

app = fastapi.FastAPI()

def predict_cluster(data: dict):
    with open('RandomForestRegressor.joblib', 'rb') as file:
        model = joblib.load(file)

    features_order = [
        'sub_type', 'listing_type', 'tom', 'building_age',
        'total_floor_count', 'floor_no', 'room_count', 'size',
        'heating_type', 'price_currency', 'city', 'district', 'neighborhood'
    ]

    X = pd.DataFrame([data], columns=features_order)
    prediction = model.predict(X)

    return prediction[0]

@app.post("/predict")
def predict_class(data: DataRequest):
    return predict_cluster(data.dict())
