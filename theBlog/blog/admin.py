from django.contrib import admin
from blog.models import BlogPost

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('js/blog.js', )

admin.site.register(BlogPost, BlogAdmin)