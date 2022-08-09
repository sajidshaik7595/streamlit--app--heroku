# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 09:37:24 2022

@author: sajid
"""

import numpy as np
import pickle 

loaded_model = pickle.load(open('C:/Users/sajid/OneDrive/Desktop/myfirst web app/diabetes_model.sav','rb'))


input_data = (1,85,66,29,0,26.6,0.351,31)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)
# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
#standardize the input data
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] ==1):
    print("The person is not diabetic")
else:
    print("The person is diabetic")