from django.shortcuts import render, HttpResponse




def home(request):
    return render(request,'home.html')


def e_books_creation(request):
    return render(request, 'ebook.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')
