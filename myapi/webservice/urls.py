from django.urls import path, include
from .views import index, getPosts

urlpatterns = [
    path('', index, name='index_page'),
    path('soap/', getPosts, name='soap_api'),
]