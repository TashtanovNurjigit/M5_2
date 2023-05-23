from django.urls import path
from . import views

urlpatterns = [
    path('movie/', views.movie_list_api_view),
    path('movie/<int:id>/', views.movie_detail_api_view),
]
