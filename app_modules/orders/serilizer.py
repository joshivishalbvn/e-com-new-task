import json
from rest_framework import serializers 
from app_modules.orders import models
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from app_modules.orders.task import send_order_confirmation_email
from app_modules.products.models import Products
from django.contrib.auth import get_user_model
from django.db.models import Sum

from app_modules.products.serilizer import ProductSerailizer
 
user = get_user_model()

class OrderSerailizer(serializers.ModelSerializer):

    order_products = serializers.ListField(required = False)

    class Meta:
        model = models.Order
        fields = (
            "customer",
            "order_products"
        )

    def _get_total_amount(self,product_id_list):
        total =  models.Products.objects.filter(id__in=product_id_list).aggregate(total=Sum("price"))["total"]
        print('\033[91m'+'total: ' + '\033[92m', total)
        return total

    def create(self, validated_data):
        order_products = validated_data.pop("order_products",[])
        customer_obj = validated_data.pop("customer",None)
        if not order_products:
            raise ValidationError("One Product Is Required To Create An Order...")
        
        order_products = [json.loads(order) for order in order_products]
        product_id_list = [product["id"] for product in order_products]

        order_obj = models.Order(customer=customer_obj,total_amount=self._get_total_amount(product_id_list))
        order_obj.save()
        
        for product in order_products:
            product_id=product["id"]
            order_product_serailizer = OrderProductSerializer(data=product)
            order_product_serailizer.is_valid(raise_exception=True)
            try:
                product_obj = Products.objects.get(id=product_id)
                order_product_obj = models.OrderItems(
                    product=product_obj,
                    quantity = product["quantity"],
                    price = product_obj.price,
                    order = order_obj
                )
                product_obj.stock -=  product["quantity"]
                product_obj.save()
                order_product_obj.save()
            except Exception as e:
                print('\033[91m'+'e: ' + '\033[92m', e)
                raise ValidationError("Product not found please try again later...")
        send_order_confirmation_email(order_obj.id)
        return order_obj
    
class OrderDataSerailizer(serializers.ModelSerializer):

    order_products = serializers.SerializerMethodField()

    class Meta:
        model = models.Order
        fields = (
            "id",
            "customer",
            "order_products",
            "total_amount",
        )

    def get_order_products(self,obj):
        try:
            products = models.OrderItems.objects.filter(order=obj)
            print('\033[91m'+'products: ' + '\033[92m', products)
            return OrderProductDataSerailiser(products,many=True).data
        except Exception as e:
            print('\033[91m'+'e: ' + '\033[92m', e)
            return []

    
class OrderProductSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate(self, attrs):
        product_id = attrs.get("id")
        requested_quantity = attrs.get("quantity")

        if product_id is None:
            raise ValidationError("Product ID is required...")
        
        if requested_quantity is None:
            raise ValidationError("Quantity is required...")
        
        product_obj = Products.objects.filter(id=product_id).first()
        available_quantity = product_obj.stock

        if requested_quantity > available_quantity:
            raise ValidationError(f"Available Stock Is : {available_quantity}")
        
        return super().validate(attrs)
    
class OrderProductDataSerailiser(serializers.ModelSerializer):

    product = serializers.SerializerMethodField()

    class Meta:
        model = models.OrderItems
        fields = (
            "id",
            "product",
            "quantity",
            "price",
        )

    def get_product(self,obj):
        return ProductSerailizer(obj.product).data