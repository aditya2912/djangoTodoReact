# this file is created to convert the data from frontend into json to use it in backend
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
#        fields = ('id', 'title', 'description', 'completed')
        
        
#class NameSerializer(serializers.ModelSerializer):
#    class Meta: 
#        model = Name
#        fields = "__all__"
#        fields = ('name', '')
        