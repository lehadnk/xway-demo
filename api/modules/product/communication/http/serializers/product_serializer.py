from rest_framework import serializers
from rest_framework.serializers import Serializer


class ProductSerializer(Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.IntegerField()