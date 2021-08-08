from django.urls import path

from post.views import PostList, CreatePost, PostDetail, UserPost, DeletePost

app_name = 'post'


urlpatterns = [
    path('',PostList.as_view(),name='all'),
    path('new/',CreatePost.as_view(),name='create'),
    path('by/<username>/',UserPost.as_view(),name='for_user'),
    path('by/<username>/<pk>',PostDetail.as_view(),name='single'),
    path('delete/<pk>',DeletePost.as_view(),name='delete'),
]