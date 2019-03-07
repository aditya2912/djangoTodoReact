from django.contrib import admin
from .models import Todo
# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    name_display = ('title')
    
#class NameAdmin(admin.ModelAdmin):
#    name_display = ('name')
    

#admin.site.register(Name, NameAdmin)    
    
admin.site.register(Todo, TodoAdmin)