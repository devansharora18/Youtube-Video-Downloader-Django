from django.shortcuts import render

# Create your views here.

def ytd(request):
	return render(request, 'ytd.html')