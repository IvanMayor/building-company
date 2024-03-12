from django.urls import path, include

from .views import BuildingView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"buildings", BuildingView)


urlpatterns = [path("", include(router.urls))]

app_name = "building"
