from . import views
from django.urls import path

app_name="collections"

urlpatterns = [
    # 조회랑 생성 합쳐도 될듯 ?
    path('', views.collections_list, name="collectionslist"),
    path('create/', views.create_collection, name="create"),
    path('<int:collection_pk>/', views.collection_detail, name="detail"),
    path('<int:collection_pk>/like/', views.like_collection, name="likes"),
    path('<int:collection_pk>/comments/', views.comments_list, name="comments"),
    path('<int:collection_pk>/comments/<comment_pk>/', views.comment_status, name="comment_ud"),
]
