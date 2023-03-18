from django.urls import  path
from . import views

urlpatterns = [
    path('employees/', views.EmployeesView.as_view()),
    path('employee/<int:id>/', views.EmployeeView.as_view()),
    path('documents/', views.DocumentsView.as_view()),
    path('documents/<int:id>/', views.DocumentView.as_view()),
    path('posts/', views.PostsView.as_view()),
    path('posts/<int:id>/', views.PostView.as_view()),
    path('pages/', views.PagesHTMLView.as_view()),
    path('pages/<str:id>/', views.PageHTMLView.as_view()),
]