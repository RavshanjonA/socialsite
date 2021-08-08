from django.urls import path

from group.views import ListGroup, CreateGroup, SingleGroup, JoinGroup, LeaveGroup

app_name = 'group'

urlpatterns = [
    path('', ListGroup.as_view(), name='all'),
    path('new/', CreateGroup.as_view(), name='create'),
    path('posts/in/<slug>', SingleGroup.as_view(), name='single'),
    path('join/<slug:slug>', JoinGroup.as_view(), name='join'),
    path('leave/<slug:slug>', LeaveGroup.as_view(), name='leave'),
]
