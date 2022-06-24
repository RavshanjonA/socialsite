
from django.contrib import admin
from django.urls import path, include
from core.views import HomePage, TestPage, ThanksPage
from django.contrib.auth import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('account/', include('django.contrib.auth.urls')),
    path('group/', include('group.urls',namespace='group')),
    path('post/', include('post.urls',namespace='post')),
    path('test/',TestPage.as_view(),name='test'),
    path('thanks/',ThanksPage.as_view(),name='thanks'),
    path('', HomePage.as_view(), name='home'),

]
