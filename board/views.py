from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView
                                  )
from .models import Post
from .filters import PostFilter
from .forms import PostForm, EditForm

class PostListView(ListView):
    model = Post
    template_name = 'notice_board/post_list.html'
    # context_object_name = 'posts'
    ordering = ['-post_created']
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = PostFilter(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = PostFilter(self.request.GET, queryset)
        context["filter"] = filter
        return context


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
    #template_name = 'notice_board/post_form.html'
    # 빈 폼이 출력됌, post_form_django.html의 form.html의 html 요소가 post_form과 동일해서 작동은 됐음.

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'notice_board/post_confirm_delete.html'
    success_url = reverse_lazy('board:notice-board')