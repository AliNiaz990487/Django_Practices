from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('reset-password/', views.reset_password, name='reset-password'),
    path('set-new-password', views.set_new_password, name="set-new-password"),
    path('change-password', views.change_password, name='change-password')
]