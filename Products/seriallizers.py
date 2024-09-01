from rest_framework import serializers
from  Products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['id','name', 'image', 'description', 'price', 'discount', 'discountAmount', 'category']
