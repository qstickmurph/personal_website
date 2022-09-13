from django.shortcuts import render

# Create your views here.
def HomeView(request):
     return render(request, 'home.html')

def AboutView(request):
     return render(request, 'about.html')

def ContactView(request):
     return render(request, 'contact.html')

def ResumeView(request):
     return render(request, 'resume.html')

