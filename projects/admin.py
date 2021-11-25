from django.contrib import admin
from . models import Project,Review,Tag

# Register your models here.



class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    date_hierarchy = 'created'
    ordering = ('-created',)
 
    
     

class Reviewadmin(admin.ModelAdmin):
    list_display = ('project', 'value')
   
    

admin.site.register(Project, ProjectAdmin)
admin.site.register(Review, Reviewadmin)
admin.site.register(Tag)


