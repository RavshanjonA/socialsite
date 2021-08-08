from braces.views import SelectRelatedMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from post.models import Post

User = get_user_model()

class PostList(ListView, SelectRelatedMixin):
    model = Post
    select_related = ('user','group')


class UserPost(ListView):
    model = Post
    template_name = 'post/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context

class PostDetail(DetailView, SelectRelatedMixin):
    model = Post
    select_related = ('user','group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact = self.kwargs.get('username'))

class CreatePost(SelectRelatedMixin,LoginRequiredMixin,CreateView):
    fields = ('message','group')
    model = Post

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeletePost(SelectRelatedMixin,LoginRequiredMixin,DeleteView):
    model = Post
    select_related = ('user','group')
    success_url = reverse_lazy('post:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete( *args, **kwargs)