from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def index(request):
	return HttpResponse("<h1> <marquee bgcolor='pink'> <p style='color:red'><a href='http://www.yahoo.com'>Hay! Click Me!</a></p> </marquee></h1>")