import json
import logging

from django.db import transaction
from rest_framework.viewsets import ModelViewSet

from catalogue.helpers.HttpException import HttpException
from catalogue.helpers.HttpResponseHandler import HTTP
from catalogue.helpers.Producer import Producer
from catalogue.helpers.SchemaValidator import SchemaValidator
from catalogue.models import Category
from catalogue.models.catalogue import Catalogue
from catalogue.models.video_categories import VideoCategory
from catalogue.serializers.catalogueSerializer import CatalogueSerializer

logger = logging.getLogger(__name__)


class CatalogueViewSet(ModelViewSet):

    def create(self, request):
        try:
            SchemaValidator.validate_obj_structure(request.data, 'catalogue_post.json')

            if 'file' not in request.FILES:
                raise Exception('You need to send a file.')

            list_of_caterogies = [int(x) for x in request.data['category'].split(",")]


            new_video = Catalogue(
                title=request.data['title'],
                year=int(request.data['year']),
                description=request.data['description'],
                rating=0,
            )

            for image in request.FILES.getlist('file'):
                # Save the image using the model's ImageField settings
                filename = image.name
                new_video.image.save("%s" % filename, image)
            with transaction.atomic():
                producer = Producer(host='localhost', channel='wish')
                caterogies = list(Category.objects.filter(id__in=list_of_caterogies).all())
                new_video.category.add(*caterogies)
                new_video.save()
                message = {}
                message['categories'] = list_of_caterogies
                producer.send_message(message=json.dumps(list_of_caterogies), queue='wish')

            logger.info("New Video")

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Ocorreu um erro   inesperado',
                                 'Unexpected Error. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, "Amazing")

    def list(self, request):
        query = Catalogue.objects.all()
        data = CatalogueSerializer(query, many=True).to_representation(query)
        return HTTP.response(200, "Amazing", data=data)
