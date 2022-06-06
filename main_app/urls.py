from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('clients/', views.ClientList.as_view(), name="client_list"),
    path('clients/new/', views.ClientCreate.as_view(), name="client_create"),
    path('clients/<int:pk>/', views.ClientDetail.as_view(), name="client_detail"),
    path('clients/<int:pk>/update',
         views.ClientUpdate.as_view(), name="client_update"),
]
