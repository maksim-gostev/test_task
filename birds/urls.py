from django.urls import path

from birds import views

urlpatterns = [
    path('bird/create/', views.BirdCreateView.as_view(), name='bird_create'),
    path('bird/<int:pk>/', views.BirdDetailView.as_view(), name='bird_detail'),
    path('bird/', views.BirdListView.as_view(), name='bird_list'),
]