from django.urls import path

from .views import HomeView, AboutView, ResumeView, ContactView

urlpatterns = [
    path('', HomeView, name='home'),
    path('about/', AboutView, name='about'),
    path('resume/', ResumeView, name='resume'),
    path('contact/', ContactView, name='contact'),
]