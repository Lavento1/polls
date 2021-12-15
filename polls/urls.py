from django.urls import path
from polls import views


app_name = 'polls'  # app_name 변수에 poll 앱 저장

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail')
]