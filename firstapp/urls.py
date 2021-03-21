from django.urls import path
from .views import register_view, logout_view, Home, profile

urlpatterns = [
    path('home/', Home, name='home'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('accounts/profile/', profile, name='profile')

]