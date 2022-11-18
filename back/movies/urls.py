from . import views
from django.urls import path

app_name="movies"

urlpatterns = [
    path('', views.movie_list, name="movies"),
    path('<int:movie_pk>/', views.movie_detail, name="detail"),
    path('<int:movie_pk>/like/', views.like_movie, name="likes"),
    path('<int:movie_pk>/reviews/', views.movie_reviews, name="reviews"),
    path('<int:movie_pk>/collections/', views.movie_collections, name='collections'),
    path('search/<keyword>/', views.auto_complete),
]
