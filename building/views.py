from django.shortcuts import render
from rest_framework import viewsets

from building.models import Building


class BuildingView(viewsets.ModelViewSet):
    queryset = Building.objects.all()
