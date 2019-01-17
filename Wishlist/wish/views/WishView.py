import logging
import re

from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from wish.helpers.HttpException import HttpException
from wish.helpers.SchemaValidator import SchemaValidator

from wish.helpers.HttpResponseHandler import HTTP
from wish.models.wish import Wish
from wish.serializers.WishSerializer import WishSerializer, WishEmailSerializer

logger = logging.getLogger(__name__)


class WishViewSet(GenericViewSet):

    def list(self, request):
        try:
            query = Wish.objects.filter(user_id=request.USER_ID).all()
            data = WishSerializer(query, many=True).to_representation(query)
            return HTTP.response(200, 'Wish View', data)

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Some error occurred. {}. {}.'.format(type(e).__name__, str(e)))

    def create(self, request):
        try:
            # Check for Schema
            SchemaValidator.validate_obj_structure(request.data, 'wish.json')
            # 1. Check if pair username-password is correct
            category_id = [category for category in request.data['categories']]
            user_id = request.USER_ID
            user_email = request.USE_EMAIL
            with transaction.atomic():
                Wish.objects.filter(user_id=user_id).all().delete()
                for category in category_id:
                    Wish(
                        category_id=category,
                        user_id=user_id,
                        user_email=user_email
                    ).save()
                logger.info("New wishes for user_id: {}".format(user_id))

        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Ocorreu um erro   inesperado',
                                 'Unexpected Error. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, 'Wishes Updated')

    def get_user_email(self, request):
        try:
            categories = re.findall(r'\d+', request.query_params['categories'])
            query = Wish.objects.filter(category_id__in=categories).values('user_email').all()
            data = WishEmailSerializer(query, many=True).to_representation(query)
            return HTTP.response(200, 'Wish View', data)
        except ObjectDoesNotExist:
            return HTTP.response(404, 'No Users Found')
