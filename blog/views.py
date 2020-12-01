# from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import PostForm


class NewPost(CreateView):
    form_class = PostForm
    success_url = 'profile'
    template_name = 'new_post.html'
