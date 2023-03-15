from django.shortcuts import render

# Create your views here.
def tomato(request):
    return render(request,'tomato.html')
def banana(request):
    return render(request,'banana.html')
