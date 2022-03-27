from django.urls import path
from rest_framework.authtoken import views
from .api import api


urlpatterns = [
    path('login', views.obtain_auth_token, name="login"),
    path('route-detail', api.RouteDetails.as_view(), name='route-detail'),
    path('route-detail/<str:loopback>', api.RouteDetails.as_view(), name='route-detail'),
    path('route-detail/<str:loopback_start>/<str:loopback_end>', api.RouteDetails.as_view(), name='route-detail'),
]