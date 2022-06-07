from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('clients/', views.ClientList.as_view(), name="client_list"),
    path('clients/new/', views.ClientCreate.as_view(), name="client_create"),
    path('clients/<int:pk>/', views.ClientDetail.as_view(), name="client_detail"),
    path('clients/<int:pk>/update',
         views.ClientUpdate.as_view(), name="client_update"),
    path('clients/<int:pk>/delete',
         views.ClientDelete.as_view(), name="client_delete"),
    path('clients/<int:pk>/interviews/new/',
         views.InterviewCreate.as_view(), name="interview_create"),
    path('interviews/<int:pk>/update',
         views.InterviewUpdate.as_view(), name="interview_update"),
    path('interviews/<int:pk>/delete',
         views.InterviewDelete.as_view(), name="interview_delete"),
    path('accounts/signup/', views.Signup.as_view(), name="signup")

]
