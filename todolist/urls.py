from django.urls import path
from todolist.views import show_todolist, register,login_user,logout_user, create_task
from todolist.views import update_task, delete_task, show_todolist_json, add_task

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name="show_todolist"),
    path('login/', login_user, name='login'), 
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create-task'),
    path('logout/', logout_user, name='logout'),
    path('deletetask/<int:id>', delete_task, name='deletetask'),
    path('updatetask/<int:id>', update_task, name='updatetask'),
    path('json/', show_todolist_json, name='show-todolist-json'),
    path('add/', add_task, name='add'),
]
