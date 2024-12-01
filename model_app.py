from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

class Input(BaseModel):
    Gender : str
    Age : int
    Driving_License : int
    Region_Code : float
    Previously_Insured : int
    Vehicle_Age : str
    Vehicle_Damage : str
    Annual_Premium : float
    Policy_Sales_Channel : float
    Vintage : int


class Output(BaseModel):
    Response :int

@app.post("/predict",response_model = Output)
def predict(data_input:Input) -> Output:
    x_input = pd.DataFrame([{
        'Gender' : data_input.Gender,
        'Age' : data_input.Age,
        'Driving_License' : data_input.Driving_License,
        'Region_Code' : data_input.Region_Code,
        'Previously_Insured' : data_input.Previously_Insured,
        'Vehicle_Age' : data_input.Vehicle_Age,
        'Vehicle_Damage' : data_input.Vehicle_Damage, 
        'Annual_Premium' : data_input.Annual_Premium,
        'Policy_Sales_Channel' : data_input.Policy_Sales_Channel,
        'Vintage' : data_input.Vintage

    }])

    model = joblib.load('cross-sell-prediction.pkl')
    prediction = model.predict(x_input)[0]
    return Output(Response = int(prediction))