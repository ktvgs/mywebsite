from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('upload/', views.upload_image, name='upload_image'),
]