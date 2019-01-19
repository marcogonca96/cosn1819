from rest_framework import serializers
from ..models.wish import Wish


class WishSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        data = super(WishSerializer, self).to_representation(obj)  # the original data
        return data

    class Meta:
        model = Wish
        fields = '__all__'


class WishEmailSerializer(serializers.ModelSerializer):

    def to_representation(self, obj):
        data = super(WishEmailSerializer, self).to_representation(obj)  # the original data
        return data

    class Meta:
        model = Wish
        fields = ['user_email']

