from django.urls import path

from profiles import views

urlpatterns = [
    path('create/', views.CreateProfile.as_view(), name='profile-create'),
    path('edit/', views.EditProfile.as_view(), name='profile-edit'),
    path('delete/', views.delete_profile, name='profile-delete'),
    path('details/', views.details_profile, name='profile-details')
]