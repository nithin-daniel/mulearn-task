from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('signin/',views.signin,name="signin"),
    path('logout/',views.logout_view,name="logout"),
    path('add-task/',views.add_task,name="add_task"),
    path('completed/<int:id>',views.completed,name="completed"),
    path('completed_delete/<int:id>',views.completed_delete,name="completed_delete"),
]
