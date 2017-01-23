from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hola y bienvenido al indice de mi proyecto")

# Create your views here.
