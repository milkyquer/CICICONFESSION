
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('wall/', views.community_wall, name='community_wall'),
    path('report/<int:post_id>/', views.report_post, name='report_post'),
]
