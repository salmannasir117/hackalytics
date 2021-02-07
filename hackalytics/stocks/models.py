from django.db import models
from enum import Enum


# Create your models here.

#enum for the types of data to visualize
class DataSeries(Enum):
    REAL_GDP = "real GDP"
    NOMINAL_GDP_CONVERTED = "nominal GDP converted from real GDP"
    NOMINAL_GDP_RAW = "nominal GDP" 

#enum for types of hyperparameters used to train model
class ParameterSets(Enum):
    TRADITIONAL = "Traditional"
    NOVEL = "Novel"
    UNORTHODOX = "Unorthodox"

#database to store a graph and its data, data series, and parameter types
class GraphData(models.Model):
    data = models.FileField(upload_to="../static/stocks")
    data_series = models.CharField(max_length=200, choices=[(tag.value, tag.name) for tag in DataSeries], blank=True)
    parameter_set = models.CharField(max_length=200, choices=[(tag.value, tag.name) for tag in ParameterSets], blank=True)