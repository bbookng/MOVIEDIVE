from . import views
from django.urls import path

app_name="community"

urlpatterns = [
    path('<int:movie_pk>/', views.review_list, name="reviews"),
    path('<int:movie_pk>/create', views.create_review, name="create"),
    path('<int:movie_pk>/<int:review_pk>/', views.review_detail, name="detail"),
    path('<int:movie_pk>/<int:review_pk>/like/', views.like_review, name="likes"),
    path('<int:movie_pk>/<int:review_pk>/comments/', views.comments_list, name="comments"),
    path('<int:movie_pk>/<int:review_pk>/comments/<comment_pk>/', views.comment_status, name="comment_ud"),
]
