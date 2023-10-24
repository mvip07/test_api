from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import TodoModel
from .serializers import TodoSerializer

class ListTodoView (ListAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer

class DetailTodoView (RetrieveAPIView):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer