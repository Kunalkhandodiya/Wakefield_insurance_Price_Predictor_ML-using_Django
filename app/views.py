from django.shortcuts import render
import pickle
import array
import numpy as np

def predictor(request):
    if request.method == "POST":
        # Get values from the form
        age = int(request.POST.get('age'))
        bmi = float(request.POST.get('bmi'))
        sex = int(request.POST.get('sex'))
        children = int(request.POST.get('Childern'))
        smoker = int(request.POST.get('Smoker'))
        region = int(request.POST.get('Region'))

        # Load model
        with open('C:/Users/Kunal/OneDrive/Desktop/wakefield_insurance/app/data/gb_model1.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
        
        # Prepare input and predict
        features = [[age, bmi, sex, children, smoker, region]]
        prediction = loaded_model.predict(features)[0]
        
        return render(request, "app/templates/index.html", {"result": prediction})

    return render(request, "app/templates/index.html")
