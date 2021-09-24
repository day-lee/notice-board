from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView
                                  )
from .models import Post
from .forms import PostForm, EditForm

class PostListView(ListView):
    model = Post
    template_name = 'notice_board/post_list.html'
    # context_object_name = 'posts'
    ordering = ['-post_created']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    template_name = 'notice_board/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'notice_board/post_form.html'
    fields = '__all__'
    #form_class = PostForm #returns 'FileField' object has no attribute 'use_required_attribute' error


class PostTestView(CreateView):
    model = Post
    template_name = 'notice_board/form_js_test.html'
    fields = '__all__'


class PostUpdateView(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'notice_board/post_form_django.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'notice_board/post_confirm_delete.html'
    success_url = reverse_lazy('board:notice-board')