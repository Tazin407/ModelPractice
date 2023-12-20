from django.shortcuts import render
# from .models import Employee
# from .forms import EmpData
from .import models, forms

# Create your views here.
def home(request):
    if request.method== 'POST':
        emp= forms.EmpData(request.POST)
        return render(request, 'index.html',{"emp":emp})

    emp= forms.EmpData()
    return render(request, 'index.html',{"emp":emp}) 