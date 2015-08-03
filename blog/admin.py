from django.contrib import admin
from .models import Post

# Register your models here.l

class PostAdmin(admin.ModelAdmin):

    # fields display on change list
    list_display = ['title', 'description']

    # fields to filter the change list with
    list_filter = ['published', 'created_on']

    # fields to search in change list
    search_fields = ['title', 'description', 'content', 'creadted_by']

    # enable the date drill down on change list
    date_hierarchy = 'created_on'

    # enable the save buttons on top on change form
    save_on_top=True

    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Post, PostAdmin)
    
