from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    name = serializers.CharField()
    price = serializers.IntegerField()
    origin_country = serializers.CharField()
    create_date = serializers.DateTimeField()
    stock = serializers.IntegerField()
    category = serializers.CharField()
