from django.urls import path
from todo.views import add_view, detailed_view, update_view, delete_view, mass_delete_view


urlpatterns = [
    path('task/add/', add_view, name='task_add'),
    path('task/<int:pk>', detailed_view, name='task_detail'),
    path('task/<int:pk>/update/', update_view, name='task_update'),
    path('task/<int:pk>/delete/', delete_view, name='task_delete'),
    path('task/mass_delete/', mass_delete_view, name='task_mass_delete'),
]