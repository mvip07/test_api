from rest_framework import serializers
from .models import TodoModel


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ('id', 'title', 'body')