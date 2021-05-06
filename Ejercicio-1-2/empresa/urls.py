from django.urls import path
from .api import *
urlpatterns = [
    path('api',EmpresaApi.as_view()),
    path('api/create',EmpresaCreateApi.as_view()),
    path('api/<int:pk>',EmpresaUpdateApi.as_view()),
    path('api/<int:pk>/delete',EmpresaDeleteApi.as_view()),
    
]