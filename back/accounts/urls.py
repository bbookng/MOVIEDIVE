from . import views
from django.urls import path

app_name="accounts"

urlpatterns = [
    path("currentuser/", views.get_current_user_profile),
    path('profile/set_nickname/', views.set_nickname),
    path('profile/set_message/',  views.set_message),
    path('profile/update/', views.profile),
    path('profile/<int:user_pk>/follow/', views.follow),
    path("profile/<username>/", views.profile),
    path('profile/<username>/movies/', views.get_likelists),
    path('profile/<username>/reviews/', views.get_user_reviews),
    path('profile/<username>/collections/', views.get_user_collections),
]
