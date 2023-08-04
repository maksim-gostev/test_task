from django.urls import path
from birds_seen import views

app_name = 'birds_seen'

urlpatterns = [
    path('saw/<int:pk>/', views.SawView.as_view(), name='saw'),
    path('saw/', views.Birds_I_saw_View.as_view(), name='saw_list'),
]