# -*- coding: utf-8 -*-

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from fastAPI import LandSlide
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("ML_MODEL/random_forest_model.pkl","rb")
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To ResQCode':f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted LandSlide with the confidence
@app.post('/predict')
def predict_landslide(data:LandSlide):
    data = data.dict()
    print(data)
    print("Hello")
    landslide=data['Landslide']
    aspect=data['Aspect']
    curvature=data['Curvature'] 
    earthquake=data['Earthquake']
    elevation=data['Elevation']
    flow=data['Flow']
    lithology=data['Lithology']
    ndvi=data['NDVI']
    ndwi=data['NDWI']
    plan=data['Plan']
    precipitation=data['Precipitation']
    profile=data['Profile']
    slope=data['Slope']
   # print(classifier.predict([[landslide, aspect, curvature, earthquake, elevation]]))
    prediction = classifier.predict([[landslide, aspect, curvature, earthquake, elevation, flow, lithology, ndvi, ndwi, plan, precipitation, profile, slope]])
    if(prediction[0]>0.5):
        prediction="Landslide has occured"
    else:
        prediction="Landslide hasn't occured"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload