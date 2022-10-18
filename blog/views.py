from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import sqlite3
# Create your views here.
def home(request):
    return HttpResponse('Welcome to our site!')
    
