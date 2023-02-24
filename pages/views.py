from django.shortcuts import render

# Create your views here.
def HomeView(request):
     return render(request, 'pages/home.html')

def AboutView(request):
     return render(request, 'pages/about.html')

def ContactView(request):
     return render(request, 'pages/contact.html')

def ResumeView(request):
     return render(request, 'pages/resume.html')

