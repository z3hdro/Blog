from django.urls import path
from blog.views import blog_list


urlpatterns = [
        path('', blog_list, name='blog_list'),
        path('index/', blog_list, name='blog_list')
        ]
