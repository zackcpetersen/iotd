from rest_framework import routers

from images.api import viewsets as image_views

router = routers.DefaultRouter()

router.register(r'images', image_views.ImageViewSet)
