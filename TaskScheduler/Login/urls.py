from django.urls import path
from . import views

urlpatterns = [
    #path('login/', views.UserList, name='login'),
    # Add other URL patterns as needed

    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]