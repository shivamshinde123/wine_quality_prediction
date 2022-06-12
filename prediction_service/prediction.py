from src.get_data import read_params
import joblib
import numpy as np
from flask import request
import yaml
import os
import joblib
import json

params_path = "params.yaml"
schema_path = os.path.join("prediction_service", "schema_in.json")

class NotInRange(Exception):

    def __init__(self,message="Value entered are not in range"):
        self.message = message
        super().__init__(self.message)

class NotInCols(Exception):

    def __init__(self,message="Not in columns"):
        self.message = message
        super().__init__(self.message)

def Predict(data):
    config = read_params(params_path)
    model_dir_path = config['webapp_model_dir']
    model = joblib.load(model_dir_path)
    predictions = model.predict(data).tolist()[0]

    try:
        if 3 <= predictions <= 8:
            return predictions
        else:
            raise NotInRange
    
    except NotInRange:
        return "Unexpected result"


def get_schema(schema_path=schema_path):
    with open(schema_path) as json_file:
        schema = json.load(json_file)
        return schema


def validate_input(dict_request):

    def validate_cols(col):
        schema = get_schema()
        actual_cols = schema.keys()
        if col not in actual_cols:
            raise NotInCols
    
    def validate_values(col,val):
        schema = get_schema()
        if not (schema[col]['min'] <= float(dict_request[col]) <= schema[col]['max']):
            raise NotInRange

    
    for col, val in dict_request.items():
        validate_cols(col)
        validate_values(col, val)

    return True

def form_response(dict_request):
    try:
        if validate_input(dict_request):
            data = dict_request.values()
            data = [list(map(float, data))]
            response = Predict(data)
            return response
    
    except NotInRange as e:
        response = {"The excepted range": get_schema(), 'response': str(e)}
        return response

    except NotInCols as e:
        response = {'The expected columns': get_schema().keys(), 'response': str(e)}
        return response

def api_response(dict_request):
    try:
        if validate_input(dict_request):
            data = np.array([list(dict_request.values())])
            response = Predict(data)
            response = {'response':response}
            return response

    except NotInRange as e:
        response = {"The excepted range": get_schema(), 'response': str(e)}
        return response

    except NotInCols as e:
        response = {'The expected columns': get_schema().keys(), 'response': str(e)}
        return response