# Create your views here.
from django.views.generic import ListView, TemplateView
# from posts.forms import AddCommentaryForm
from posts.models import Post
 
class PostList(ListView):
    template_name = 'postlist.html'
    model = Post

# added for the section "The post view"
class PostDetails(TemplateView):
  template_name = 'postdetails.html'
 
  def post(self, request, *args, **kwargs):
    return self.get(request, *args, **kwargs)
 
  # Overriding
  def get_context_data(self, **kwargs):
    context = super(PostDetails, self).get_context_data(**kwargs)
 
    post = self.get_post(kwargs['slug'])
    form = self.get_form(post)
 
    context.update({'form':form, 'post':post})
 
    return context
 
  # Helper
  def get_post(self, slug):
    return Post.objects.get(pk=slug)
 
  # Helper
  def get_form(self, post):
    if self.request.method == 'POST':
      form = AddCommentaryForm(self.request.POST)
      if form.is_valid():
        commentary = form.save(commit=False)
        post.commentary_set.add(commentary)
      else:
        return form
 
    return AddCommentaryForm()
