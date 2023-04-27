from rest_framework.routers import DefaultRouter
from . import views
from django.urls import include, path

router = DefaultRouter()
router.register('product', views.ProductViewSet)

urlpatterns = [
    path("", include(router.urls))
]