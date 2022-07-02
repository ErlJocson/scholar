from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/education', views.educational_background_profile, name='education'),
    path('profile/guardian', views.guardian_information_profile, name='guardian'),
    path('profile/additional', views.additinal_information_profile, name='additional'),
    path('profile/requirements', views.requirements_profile, name='requirement'),
    path('profile/upload-registration', views.registration_form, name='upload-registration')
]