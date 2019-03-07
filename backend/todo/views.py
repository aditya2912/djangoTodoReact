from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
# Create your views here.

class TodoView(viewsets.ModelViewSet):
    print("4444444444444444444444444444")
    serializer_class = TodoSerializer
    queryset =  Todo.objects.all()
    
#class NameView(viewsets.ModelViewSet):
#    print("1111111111111111111111111")
#    serializer_class = NameSerializer
#    queryset = Name.objects.all()
    
    
def saveNewPerson(request):
    print("++++++++++++++++++++=")
    print(request)
    return render(request, 'dummyPage.html', {})
#    print(request.user.name)
#    engine = create_engine('sqlite:///PersonDatabase.db')
#    Base = declarative_base()
#    Base.metadata.bind = engine
#    DBSession = sessionmaker(bind=engine)
#    session = DBSession()
#    personeData = PersonInformation(id=1, personName = )