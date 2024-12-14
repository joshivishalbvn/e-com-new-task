from rest_framework import serializers
from app_modules.products import models

class ProductSerailizer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()
    images = serializers.ListField(required=False)

    class Meta:
        model = models.Products
        fields = (
            "id",
            "name",
            "stock",
            "decription",
            "images",
        )

    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep["images"] = ProductImageSerializer(instance.product_images.all(),many=True).data
        return rep

    def create(self, validated_data):
        name = validated_data.get("name",'')
        stock = validated_data.get("stock",'')
        images_data = validated_data.pop("images",[])
        

        prod_obj = models.Products.objects.filter(name=name).first()
        if prod_obj:
            prod_obj.stock += stock
            prod_obj.save()
        else:
            prod_obj = models.Products(**validated_data)
            prod_obj.save()

        if images_data:
            for image in images_data:
             models.ProductImages.objects.create(image=image,product=prod_obj)
        return prod_obj
        
        
class ProductImageSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()

    class Meta:
        model = models.ProductImages
        fields = (
            "id",
            "image",
        )

    def to_representation(self, instance):
        rep =  super().to_representation(instance)
        rep["img"] = instance.image.url
        return rep