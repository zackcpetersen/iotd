from rest_framework import viewsets

from images.api.serializers import ImageSerializer
from images.models import Image


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
