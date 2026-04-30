from django.urls import path
from toDo.views import todo_list,todo_detail,todo_create,todo_delete,todo_toggle,todo_update

urlpatterns = [
    path("",todo_list,name = 'list_html'),
    path("create/",todo_create,name = 'todo_create'),
    path('<int:id>/',todo_detail,name = "todo_detail"),
    path("<int:id>/update/",todo_update,name = "todo_update"),
    path('<int:id>/delete/',todo_delete,name = "todo_delete"),
    path('<int:id>/toggle/',todo_toggle,name = "toggle_complete")

]