from urllib import request
from django.shortcuts import redirect, render

# Create your views here.




def home(request):
    # Your code here, e.g., to render a template
    return render(request, 'index.html')
