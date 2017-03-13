from cadastros.models import PerfilAtleta

from .serializers import PerfilAtletaSerializer
from rest_framework import viewsets

class PerfilAtletaViewSet(viewsets.ModelViewSet):
    queryset = PerfilAtleta.objects.all()
    serializer_class = PerfilAtletaSerializer