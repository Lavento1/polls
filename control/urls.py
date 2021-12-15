from django.urls import path
from control import views

# 네임 스페이스(소속 공간)
app_name = 'control'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
]