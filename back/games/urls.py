from . import views
from django.urls import path

app_name="games"

urlpatterns = [
      path('actorquiz/', views.actor_quiz, name='actorquiz'),
      path('oxquiz/', views.ox_quiz, name="oxquiz"),
      path('<int:user_pk>/exp/', views.user_exp, name="exp"),
]
