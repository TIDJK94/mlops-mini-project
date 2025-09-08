from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# load model at startup
model = joblib.load('regression.joblib')


class PredictRequest(BaseModel):
    size: float
    nbRooms: int
    hasGarden: bool


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
async def predict_price(req: PredictRequest):
    # convert boolean to int if model expects 0/1
    has_garden_numeric = 1 if req.hasGarden else 0
    y_pred = model.predict([[req.size, req.nbRooms, has_garden_numeric]])[0]
    return {"y_pred": float(y_pred)}

