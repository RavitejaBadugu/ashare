from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from predictive_functions import get_preprocessed,get_model_prediction
app=FastAPI()


class Model_data(BaseModel):
    building_id: int
    meter: int
    site_id: int
    primary_use: str
    square_feet: float
    floor_count: Optional[float]=None
    air_temperature: Optional[float]=None
    cloud_coverage: Optional[float]=None
    dew_temperature: Optional[float]=None
    precip_depth_1_hr: Optional[float]=None
    sea_level_pressure: Optional[float]=None
    wind_direction: Optional[float]=None
    wind_speed: Optional[float]=None
    day_of_week: int
    hour: int
    week_of_year: int
    week_end: int


@app.post('/predict')
async def get_predictions(input_data: Model_data):
    temp_data=get_preprocessed(input_data.dict())
    target_value=get_model_prediction(temp_data)
    return {'meter_reading':target_value}