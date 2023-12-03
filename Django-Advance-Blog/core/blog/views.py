from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView,DeleteView
from blog.models import Post
from django.shortcuts import get_object_or_404
from django.utils import timezone
from blog.forms import PostForm
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin



def blog_view(request):
    return render(request,'blog/index.html')

class PostListView(ListView):

    # model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    ordering = '-id'
    
    #def get_queryset(self):
    #   posts = Post.objects.filter(status=1)
    #   return posts

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    
class PostDetailView(PermissionRequiredMixin,LoginRequiredMixin,DetailView):
    permission_required = "blog.view_post_detail"
    model = Post
    
'''   
class PostCreateView(FormView):
    template_name = "form.html"
    form_class = PostForm
    success_url = "/blog/post/"
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)
'''

class PostCreateView(CreateView):
    model = Post
    fields = ["title","content","status",
                  "category"]
    success_url = '/blog/post/'
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/post/'
    
