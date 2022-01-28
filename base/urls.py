from django.urls import path
from . views import *
urlpatterns=[
    path('todo/get',get_todos,name='get_todos'),
    path('todo/get/<int:pk>',get_todos,name='get_todo'),
    path('todo/create',create_todo,name='create_todo')
]