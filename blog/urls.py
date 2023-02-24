from django.urls import path
from .views import BlogHomeView, BlogListView, BlogPostView

urlpatterns = [
    path('', BlogHomeView, name='blog_home'),
    path('post/', BlogPostView, name='blog_post'),
    path('list/', BlogListView, name='blog_list'),
]
