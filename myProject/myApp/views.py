from django.shortcuts import render
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

model_path = BASE_DIR/'ml_model'/'ecommerce_model.pkl'
model = joblib.load(model_path)

def home(request):
    prediction = None

    if request.method == "POST":
        profit = request.POST.get('profit')
        if profit:
            prediction = model.predict([[float(profit)]])[0]

    return render(request, 'home.html', {'prediction': prediction})