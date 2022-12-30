from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','author','status')
    prepopulated_fields = {'slug':('title',),}
    
admin.site.register(models.Category)