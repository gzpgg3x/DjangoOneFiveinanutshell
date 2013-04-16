# Create your views here.
from django.views.generic import ListView
from posts.models import Post
 
class PostList(ListView):
    template_name = 'postlist.html'
    model = Post