from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app_modules.orders import models,serilizer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class OrderViewSet(ModelViewSet):

    model_class = models.Order

    def get_serializer_class(self):
        actions = {
            "list": serilizer.OrderDataSerailizer,
            "retrieve": serilizer.OrderDataSerailizer,
            "create": serilizer.OrderSerailizer,
            "destroy": serilizer.OrderSerailizer,
            "update": serilizer.OrderSerailizer,
        }
        if self.action in actions:
            self.serializer_class = actions.get(self.action)
        return super().get_serializer_class()
    
    def get_queryset(self):
        return models.Order.objects.all()
    
    def get_serializer_context(self):
        ctx =  super().get_serializer_context()
        ctx["request"] = self.request
        ctx["user"] = self.request.user
        return ctx
    
    def create(self, request, *args, **kwargs):
        print('\033[91m'+'self.get_serializer_class: ' + '\033[92m', self.get_serializer_class)
        serializer = self.get_serializer(
            data=request.data,
            context = self.get_serializer_context(),
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "message":"Order Created Sucessfully..."
            },
            status = status.HTTP_201_CREATED
        )