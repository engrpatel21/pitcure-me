from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('profile/<int:profile_id>/add_photo/', views.add_photo, name='add_photo')
]