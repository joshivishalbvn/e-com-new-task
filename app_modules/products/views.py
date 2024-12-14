from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app_modules.products import serilizer , models
from rest_framework.response import Response 
from rest_framework import status
from django.db.models import Q
# Create your views here.

class ProductViewSet(ModelViewSet):

    serializer_class = serilizer.ProductSerailizer
    model_class = models.Products

    def get_queryset(self):
        return models.Products.objects.filter(self.get_filtered_query())
    
    def get_filtered_query(self):
        filters = Q()
        start_price = self.request.query_params.get("start_price")
        end_price = self.request.query_params.get("end_price")
        available_stock = self.request.query_params.get("available_stock")
        name = self.request.query_params.get("name")
        description = self.request.query_params.get("description")

        if start_price:
            filters &= Q(price__gte=start_price)
        if end_price:
            filters &= Q(price__lte=end_price)

        if available_stock:
            filters &= Q(stock__gte=0)

        if name:
            filters &= Q(name=name)

        if description:
            filters &= Q(decription__icontains=name)
        return filters
    
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context = self.get_serializer_context(),
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message":"Product Created Sucessfully..."
            },
            status = status.HTTP_201_CREATED
        )
    
    def destroy(self, request, *args, **kwargs):
        try:
            self.get_object().delete()
            return Response(
                {
                    "message":"Product Deleted Sucessfully..."
                },
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {
                    "message":"Product Not Found..."
                },
                status=status.HTTP_204_NO_CONTENT
            )
        
class ProductImagesViewSet(ModelViewSet):

    serializer_class = serilizer.ProductImageSerializer

    def get_queryset(self):
        product_id = self.kwargs.get("product_id")
        return models.ProductImages.objects.filter(product_id=product_id)
    