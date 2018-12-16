from rest_framework.viewsets import ModelViewSet

from catalogue.helpers.HttpException import HttpException
from catalogue.helpers.HttpResponseHandler import HTTP
from catalogue.models.catalogue import Catalogue
from catalogue.serializers.catalogueSerializer import CatalogueSerializer


class CatalogueViewSet(ModelViewSet):

    queryset = Catalogue.objects.all()
    serializer_class = CatalogueSerializer

    def create(self, request):
        return HTTP.response(405, 'You are not allowed in here son, GTFO')
