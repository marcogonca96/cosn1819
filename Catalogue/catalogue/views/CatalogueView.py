from rest_framework.viewsets import ModelViewSet

from catalogue.helpers.HttpException import HttpException
from catalogue.helpers.HttpResponseHandler import HTTP
from catalogue.models.catalogue import Catalogue
from catalogue.serializers.catalogueSerializer import CatalogueSerializer


class CatalogueViewSet(ModelViewSet):

    def list(self, request):
        try:

            query = Catalogue.objects.all()
            data = CatalogueSerializer(query, many=True).to_representation(query)
            return HTTP.response(200, 'Catalogue View', data)

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

    def create(self, request):
        pass
