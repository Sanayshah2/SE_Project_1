
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
  return HttpResponse('index')

def test(request):
  return HttpResponse("student app is up and running")

def home(request):
  return render(request, 'students/home.html')

def login(request):
  return render(request, 'students/login.html')

def signup(request):
  return render(request, "students/signup.html")

def find_roommates(request):
  return render(request, 'students/filter_roommate.html')