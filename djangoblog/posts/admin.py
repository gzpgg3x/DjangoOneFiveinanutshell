from posts.models import Post
from django.contrib import admin

# from posts.models import Commentary
 
# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'excerpt', 'publication_date', 'owner')
 
  list_filter = ['publication_date', 'owner']
 
  date_hierarchy = 'publication_date'
 
  search_fields = ['title', 'content', 'owner__username', 'owner__first_name', 'owner__last_name']
 
  prepopulated_fields = { 'machine_name' : ('title', ) }
 
admin.site.register(Post, PostAdmin)

# class CommentaryAdmin(admin.ModelAdmin):
#   list_display = ('owner', 'post', 'publication_date')
 
#   list_filter = ['publication_date', 'owner']
 
#   search_fields = ['owner', 'content', 'post__title']
 
# admin.site.register(Commentary, CommentaryAdmin)