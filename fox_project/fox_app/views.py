from django.shortcuts import render, HttpResponse, redirect
from .models import *



def home(request):
    return render(request,'home.html')


def e_books_creation(request):
    return render(request, 'ebook.html')

def contact(request):
    if request.method == 'POST':
        print(request.POST)
        name  = request.POST.get('name')
        email  = request.POST.get('email')
        subject  = request.POST.get('subject')
        message  = request.POST.get('message')
        print(message,subject,email,name, sep='\n')
        contactusers.objects.create(name=name,email=email,subject=subject,message=message)
        return redirect('/')
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def pricing(request):
    return render(request, 'pricing.html')

def quality_assurance(request):
    return render(request, 'Quality-assurance.html')

def content_writing(request):
    return render(request, 'content-writing.html')

def website_design(request):
    return render(request, 'website-design.html')

def time_code_audio_video(request):
    return render(request, 'time-code-audio-video.html')

def get_start(request):
    return render(request, 'get-start.html')






def view_contact_details(request):
    pass



