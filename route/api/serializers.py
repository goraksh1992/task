from rest_framework import serializers
from route.models import RouteDetailsModel


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteDetailsModel
        fields = ['id', 'sapid', 'hostname', 'loopback', 'macAddress']