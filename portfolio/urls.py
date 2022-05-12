from . import views
from django.urls import path
urlpatterns = [
    path('', views.ProjectList.as_view(), name='home'),
    path('<slug:slug>/', views.ProjectDetail.as_view(),  name='project_detail'),
]