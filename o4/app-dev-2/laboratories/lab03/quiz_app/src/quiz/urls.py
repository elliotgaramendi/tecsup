from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('exam/<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('exam/create/', views.exam_create, name='exam_create'),
    path('exam/<int:exam_id>/question/add/',
         views.question_create, name='question_create'),
]
