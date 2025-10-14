from django.urls import path

from server.apps.blog.logic import *


app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
