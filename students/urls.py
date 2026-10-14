from django.urls import path
from . import views
from .views import student_api

urlpatterns = [
     path('', views.student_list, name='student_list'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('api/students/',student_api, name='student_api'),
    path('api/students/<int:id>/', views.student_detail_api, name='student_detail_api'),
]