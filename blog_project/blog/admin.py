from django.contrib import admin
from blog.models import Post,Comment
# Register your models here.
#admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):

    list_display=['title','slug','author','publish','Created','updated','status']
    prepopulated_fields={'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
