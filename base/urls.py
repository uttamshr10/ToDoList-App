from django.urls import path
from base import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name = 'login'),
    path('logout/', views.LogoutView.as_view(next_page = 'login'), name = 'logout'),
    path('register/', views.RegisterPage.as_view(), name = 'register'),
    path('', views.taskList.as_view(), name='tasks'),
    path('task/<int:pk>', views.taskDetail.as_view(), name='task'),
    path('createtask/', views.TaskCreate.as_view(), name='createtask'),
    path('updatetask/<int:pk>/', views.TaskUpdate.as_view(), name='updatetask'),
    path('deletetask/<int:pk>/', views.TaskDelete.as_view(), name='deletetask'),
]
