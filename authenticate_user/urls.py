from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('change/', views.change_password, name='change-password'),
    path('update/', views.update_informations, name='update'),
    path('forget-password/', views.forget_password_view, name='forget-password'),
    path('forget-password-form/<int:user_id>/', views.change_password_form, name='change-password-form',)
]