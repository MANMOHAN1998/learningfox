from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('e-books/', e_books_creation),
    path('contact/', contact),
    path('about/', about),
    path('pricing/', pricing),
    path('quality-assurance/', quality_assurance),
    path('content-writing/', content_writing),
    path('website-design/', website_design),
    path('time-code-audio-video/', time_code_audio_video),
    path('get-start/', get_start),
            ]
