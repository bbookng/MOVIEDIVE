from . import views
from django.urls import path

app_name="collections"

urlpatterns = [
    # 조회랑 생성 합쳐도 될듯 ?
    path('', views.collections_list),
    path('create/', views.create_collection),
    path('create/suggest/<keyword>/', views.get_suggestions),
    path('<int:collection_pk>/', views.collection_detail),
    path('<int:collection_pk>/like/', views.like_collection),
    # path('<int:collection_pk>/comments/', views.comments_list),
    path('<int:collection_pk>/comments/create/', views.comment_create),
    path('<int:collection_pk>/comments/<comment_pk>/', views.comment_status),
    path('get/collection/main/', views.get_main_collections),
    path('<username>/likes/', views.get_user_collections), 
]
