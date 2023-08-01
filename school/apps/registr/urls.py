from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.profile, name='profile'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.auth, name='login'),
    path('logout/', views.close_auth, name='logout')
]