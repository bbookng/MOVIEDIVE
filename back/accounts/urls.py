from . import views
from django.urls import path

app_name="accounts"

urlpatterns = [
    path("currentUser/", views.get_current_user_profile, name=""),
    path('profile/<int:user_pk>/follow/', views.follow),
    path("profile/<username>/", views.get_profile, name=""),
    path('profile/<username>/movies/,', views.get_wishlists),
    path('profile/<username>/reviews/', views.get_user_reviews),
    path('profile/<username>/collections/', views.get_user_collections),
    
]
