from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .apps import PredictionConfig
import pandas as pd 

class IRIS_Model_Predict(APIView): 
    """Class based view to predict based on IRIS model"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None): 
        data = request.data
        keys = []
        values = []
        for key in data: 
            keys.append(key)
            values.append(data[key])
        X = pd.Series(values).to_numpy().reshape(1, -1)
        loaded_mlmodel = PredictionConfig.mlmodel
        y_pred = loaded_mlmodel.predict(X)
        y_pred = pd.Series(y_pred)
        traget_map = {0: 'setosa', 1:'versicolor', 2:'virginica'}
        y_pred = y_pred.map(traget_map).to_numpy()
        response_dict = {"Predicted Iris Species": y_pred[0]}
        return Response(response_dict, status=200)
