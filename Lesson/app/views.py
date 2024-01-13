from django.shortcuts import render
import Students.SokolenkoEgor.main as func

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")

n1 = input("first number: ")
n2 = input("second number: ")
print(func.FunkSubtraction(n1, n2))