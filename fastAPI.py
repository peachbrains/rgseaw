# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class LandSlide(BaseModel):
    landslide: float
    aspect: float 
    curvature:float 
    earthquake:float 
    elevation:float 
    flow: float
    lithology: float
    ndvi: float
    ndwi: float
    plan: float
    precipitation: float
    profile: float
    slope: float
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float