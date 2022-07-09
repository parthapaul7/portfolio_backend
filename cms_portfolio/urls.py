from django.urls import path
from . import views 

urlpatterns = [
    path('project', views.project_list, name='projects'),
    path('project/<int:pk>', views.project_detail, ),
]
