import logging

from rest_framework.viewsets import ModelViewSet

from catalogue.helpers.HttpException import HttpException
from catalogue.helpers.HttpResponseHandler import HTTP
from catalogue.helpers.SchemaValidator import SchemaValidator, SchemaException
from catalogue.models.catalogue import Catalogue
from catalogue.serializers.catalogueSerializer import CatalogueSerializer

logger = logging.getLogger(__name__)


class CatalogueViewSet(ModelViewSet):

    def create(self, request):
        try:
            SchemaValidator.validate_obj_structure(request.data, 'catalogue_post.json')

            if 'file' not in request.FILES:
                raise SchemaException('You need to send a file.')

            logger.info("New file")

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Ocorreu um erro   inesperado',
                                 'Unexpected Error. {}. {}.'.format(type(e).__name__, str(e)))
