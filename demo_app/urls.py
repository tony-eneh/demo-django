from django.urls import path
from .views import home, base, todos

urlpatterns = [
    path('', home, name="Home"),
    path('base/', base, name="Base page"),
    path('todos', todos)
]