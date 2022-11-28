from . import views
from django.urls import path

app_name="community"

urlpatterns = [
    path('', views.review_list, name="reviews"),
    path('<int:movie_pk>/', views.search_review, name="search"),
    path('<int:movie_pk>/<int:review_pk>/', views.review_detail, name="detail"),
    path('<int:movie_pk>/<int:review_pk>/like/', views.like_review, name="likes"),
    path('<int:movie_pk>/<int:review_pk>/comments/create/', views.comment_create),
    path('<int:movie_pk>/<int:review_pk>/comments/<comment_pk>/', views.comment_status),
]
