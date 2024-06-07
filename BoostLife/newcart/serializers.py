from rest_framework import serializers
from .models import Cart

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
class CartGetSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product_id.name', read_only=True)
    previous_price = serializers.CharField(source='product_id.item_old_price', read_only=True)

    product_image = serializers.URLField(source='product_id.image', read_only=True)
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        # Format the price to have only two digits after the decimal point
        return "{:.2f}".format(obj.price)
    class Meta:
        model = Cart
        fields = ['id', 'product_id', 'u_id', 'quantity', 'price', 'previous_price','product_name', 'product_image']