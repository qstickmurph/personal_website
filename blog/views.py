from django.shortcuts import render

# Create your views here.
def BlogHomeView(request):
     return render(request, 'blog_home.html')

def BlogPostView(request):
     return render(request, 'blog_post.html')

def BlogListView(request):
     return render(request, 'blog_list.html')