from django.urls import path
from mytodo import views  # これだけでOK

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("update_task_complete/", views.update_task_complete, name="update_task_complete"),
    path("edit/<int:task_id>/", views.edit, name="edit"), # ←この1行だけでOK
    path("delete/<int:task_id>/", views.delete, name="delete"),
]

