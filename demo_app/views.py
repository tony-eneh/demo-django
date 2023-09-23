from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Yeah you don reash!")

def base(request):
    return render(request, 'base.html')

def todos(request):
    return render(request, 'todos.html')