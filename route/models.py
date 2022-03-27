from turtle import update
from venv import create
from django.db import models


class RouteDetailsModel(models.Model):
    sapid = models.CharField(max_length=14, null=True, blank=False, unique=True)
    hostname   = models.CharField(max_length=14, null=True, blank=False, unique=True)
    loopback   = models.GenericIPAddressField(max_length=14, null=True, blank=False, unique=True)
    macAddress = models.CharField(max_length=17, null=True, blank=False, unique=True)
    is_deleted = models.CharField(max_length=5, null=True, blank=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.sapid
