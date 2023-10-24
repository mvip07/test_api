from django.urls import path
from .views import ListTodoView, DetailTodoView

urlpatterns = [
    path('todo/detail/<int:pk>/', DetailTodoView.as_view()),
    path('todo/list/', ListTodoView.as_view()),
]