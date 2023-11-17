from rest_framework import serializers
from .models import Product

class ProductSerilizer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    img = serializers.CharField(max_length=300)
    price = serializers.FloatField()
        
    def create(self, data):
        product = Product.objects.create(name=data['name'], img=data['img'], price=data['price'])
        product.save()
        return product