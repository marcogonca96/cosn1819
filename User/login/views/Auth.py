import logging

import bcrypt
import jwt
from rest_framework.viewsets import GenericViewSet

from ..helpers.HttpException import HttpException
from ..helpers.HttpResponseHandler import HTTP
from ..helpers.SchemaValidator import SchemaValidator
from django.conf import settings
from rest_framework import viewsets
from ..models.User import User

logger = logging.getLogger(__name__)


class AuthViewSet(GenericViewSet):
    @staticmethod
    def login(request):
        try:
            # Check for Schema
            SchemaValidator.validate_obj_structure(request.data, 'login.json')
            # 1. Check if pair username-password is correct
            user = User.objects.filter(email=request.data['email'].lower()).get()
            if not bcrypt.checkpw(request.data['password'].encode('utf8'), user.password.encode('utf8')):
                raise HttpException(401, 'Credenciais não válidas.')
            # 4. Generate JWT
            jwt_data = {
                'user_id': user.id,
                'email': user.email,
            }
            jwt_encoded = jwt.encode(jwt_data, settings.JWT_SECRET,
                                     algorithm=settings.JWT_ALGORITHM).decode('utf-8')
            # Send Response
            data = {
                'jwt': jwt_encoded,
                'username': user.username,
            }
            logger.info("User login: {}".format(user.email))
            return HTTP.response(200, data=data)

        except User.DoesNotExist as e:
            return HTTP.response(401, 'Utilizador não existe.', 'User not valid.')
        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Ocorreu um erro inesperado',
                                 'Unexpected Error. {}. {}.'.format(type(e).__name__, str(e)))

    @staticmethod
    def verify(request):
        try:
            # Check for Schema
            SchemaValidator.validate_obj_structure(request.data, 'login.json')
            # 1. Check if pair username-password is correct
            user = User.objects.filter(username=request.data['username'].lower()).get()
            if not bcrypt.checkpw(request.data['password'].encode('utf8'), user.password.encode('utf8')):
                raise HTTP.response(200, details=False)

            return HTTP.response(200, details=True)

        except User.DoesNotExist as e:
            return HTTP.response(200, details=False)
        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400, 'Ocorreu um erro   inesperado',
                                 'Unexpected Error. {}. {}.'.format(type(e).__name__, str(e)))
    @staticmethod
    def create(request):
        try:
            data = request.data
            # 1.2. Check schema
            SchemaValidator.validate_obj_structure(request.data, 'create_user.json')
            level = User.admin if request.data['level'].lower() == 'admin' else User.normal
            user = User(
                email=data['email'].lower() if 'email' in data else None,
                username=data['username'].lower() if 'username' in data else None,
                level=level,
                password=str(bcrypt.hashpw(request.data['password'].encode('utf8'), bcrypt.gensalt()), 'utf8'),
            )
            user.save()
            logger.info("New user: {}".format(data['email']))
        except HttpException as e:
            return HTTP.response(e.http_code, e.http_detail)
        except Exception as e:
            return HTTP.response(400,
                                 'Ocorreu um erro inesperado',
                                 'Unexpected Error. {}. {}.'.format(type(e).__name__, str(e)))

        return HTTP.response(200, 'Utilizador criado com sucesso.')
