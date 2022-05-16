from . import views
from django.urls import path



urlpatterns = [
    path('', views.home_page, name="home"),
    path('projects/', views.project_page, name="project_page"),
    path('project/<str:pk>/', views.project_details, name="project"),
    path('workhistory/', views.work_history_page, name="work_history_page"),
    # path('roles/<str:pk>/', views.roles_page, name="roles_page"),

#     path('add-project/', views.addProject, name="add-project"),
#     path('edit-project/<str:pk>/', views.editProject, name="edit-project"),

#     path('inbox/', views.inboxPage, name="inbox"),
#     path('message/<str:pk>/', views.messagePage, name="message"),

#     path('add-skill/', views.addSkill, name="add-skill"),

#     path('add-endorsement/', views.addEndorsement, name="add-endorsement"),

#     path('donation/', views.donationPage, name="donation"),

#     path('chart/', views.chartPage, name="chart"),
]
