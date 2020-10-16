from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('profile/create/', views.ProfileCreate.as_view(), name='profile_create'),
    path('profile/<int:profile_id>/add_photo/', views.add_photo, name='add_photo'),
    path('profile/<int:profile_id>', views.upload_profile_pic, name='upload_profile_pic'),
    path('profile/<int:profile_id>/pic', views.upload_pic, name='upload_pic'),
    path('profile/<int:photo_id>/detail', views.detail, name='detail'),
    path('profile/<int:photo_id>/add_caption', views.add_caption, name='add_caption'),
    path('profile/<int:photo_id>/add_comment', views.add_comment, name='add_comment')
]