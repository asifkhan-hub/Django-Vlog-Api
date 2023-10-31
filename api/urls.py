from django.urls import path
from . import views


urlpatterns = [
    path('', views.VlogList.as_view(), name='vlog-list'),
    path('vlogs/<int:pk>/', views.VlogDetail.as_view(), name='vlog-detail'),
]