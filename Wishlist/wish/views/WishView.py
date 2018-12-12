from rest_framework.viewsets import ModelViewSet, GenericViewSet

from wish.helpers import HttpException, SchemaValidator
from wish.helpers.HttpResponseHandler import HTTP
from wish.models.wish import Wish
from wish.serializers.WishSerializer import WishSerializer


class WishViewSet(GenericViewSet):

    def list(self, request):
        try:

            query = Wish.objects.all()
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
            category_id = request.data['category_id']
            user_id = request.data['user_id']

            Wish(
                category_id=category_id,
                user_id=user_id
            ).save()

        except Wish.DoesNotExist as e:
            return HTTP.response(200, details=False)
        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Ocorreu um erro   inesperado',
                                 'Unexpected Error. {}. {}.'.format(type(e).__name__, str(e)))
