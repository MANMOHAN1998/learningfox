from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('e-books/', e_books_creation),
    path('contact/', contact),
    path('about/', about),
            ]
