from . import views
from django.urls import path

app_name="movies"

urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/like/', views.like_movie),
    path('<int:movie_pk>/reviews/', views.movie_reviews),
    path('<int:movie_pk>/collections/', views.movie_collections),
    path('search/<keyword>/', views.auto_complete),
    path('new/', views.get_new_movies),
    path('random/collections/', views.random_collections),
    path('recommend/', views.recommend_movies),
]
