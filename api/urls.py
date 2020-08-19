from django.urls import path

from . import api

urlpatterns = [
    path('tasks/', api.TaskListView.as_view()),
    path('tasks/<int:pk>/', api.TaskListView.as_view()),
]
