from django.contrib import admin
from .models import Post,BlogComment

# Register your models here.
admin.site.register((BlogComment))  #when more models than use tupple ((like this))
@admin.register(Post)  #admin b change
class PostAdmin(admin.ModelAdmin):
    class Media:
        js=('tinyinject.js',)
        
    
