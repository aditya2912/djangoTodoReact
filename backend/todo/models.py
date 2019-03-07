from django.db import models
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Create your models here.
class Todo(models.Model):
    print("TestTest")
    title = models.CharField(max_length=120)
#    description = models.TextField()
#    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
#    
#class Name(models.Model):
#    name = models.CharField(max_length=100)
#    
#    def __str__(self):
#         return self.name
#    
    
#class Person(models.Model):
#    personName = models.CharField(max_length=50)
#    
#    def __str__(self):
#        return self.personName
#    
#Base = declarative_base()
#    
#class PersonInformation(Base):
#    __tablename__ = 'person'
#    personId = Column(Integer, primary_key = True)
#    personName = Column(String, nullable=False)
#    
#personEngine = create_engine('sqlite:///PersonDatabase.db')
#
#Base.metadata.create_all(personEngine)    
#    

    
