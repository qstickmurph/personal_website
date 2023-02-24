from django.shortcuts import render

# Create your views here.
def BlogHomeView(request):
     return render(request, 'blog/home.html')

def BlogPostView(request):
     return render(request, 'blog/post.html')

def BlogListView(request):
     return render(request, 'blog/list.html')