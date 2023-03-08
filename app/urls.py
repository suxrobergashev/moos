from django.urls import path
from .views import home_views,about_views,blog_views,blog_detail_views,contact_views

urlpatterns = [
    path('', home_views, name='home'),
    path('about/', about_views, name='about'),
    path('contact/', contact_views, name='contact'),
    path('blog/', blog_views, name='blog'),
    path('blog/<int:pk>/',blog_detail_views, name='blog_detail'),


]
