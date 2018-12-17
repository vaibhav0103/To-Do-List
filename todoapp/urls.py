from django.urls import path, include
from todoapp.views import todoView, addTodo, deleteTodo
from django.views.generic.base import TemplateView

urlpatterns = [
    
    # to do list view and operations
    path('', todoView, name='todo'),
    path('addTodo/', addTodo, name='addtodo'),
    path('deleteTodo/<int:todo_id>/', deleteTodo, name='deletetodo'),
]