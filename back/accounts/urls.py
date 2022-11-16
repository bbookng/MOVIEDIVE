from . import views
from django.urls import path

app_name="accounts"

urlpatterns = [
    path("currentUser/", views.get_current_user_profile, name="currentUser"),
    path('profile/update/', views.update_profile, name="update"),
    path('profile/<int:user_pk>/follow/', views.follow, name="follow"),
    path("profile/<username>/", views.get_profile, name="profile"),
    path('profile/<username>/movies/', views.get_likelists, name="likelists"),
    path('profile/<username>/reviews/', views.get_user_reviews, name="reviews"),
    path('profile/<username>/collections/', views.get_user_collections, name="collections"),
]
