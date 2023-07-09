from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns =[
    path("", ListTodo.as_view(), name="task-list"),
    path("<int:pk>/", DetailTodo.as_view(), name="task-detail"),
]