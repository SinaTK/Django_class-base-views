from typing import Any
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from .serializers import CarSerializer
from home.models import Car
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin, CreateModelMixin, UpdateModelMixin, ListModelMixin
from rest_framework.response import Response

class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    

class SingleCarView(RetrieveAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    # lookup_field = 'brand'    # for use any thing else pk


class DeleteCarView(DestroyAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    
class CreateCarView(CreateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()
    
class UpdateCarView(UpdateAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


class GenericHomeView(RetrieveModelMixin, ListModelMixin, DestroyModelMixin, CreateModelMixin, UpdateModelMixin, GenericAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.brand == 'Kia':
            return Response('Sorry, this cart is not available...')
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def get(self, request, pk=None, *args, **kwarg):
        if pk is not None:
            return self.retrieve(request, *args, **kwarg)
        else:
            return self.list(request, *args, **kwarg)
    
    def delete(self, request, *args, **kwarg):
        return self.destroy(request, *args, **kwarg)
    
    def post(self, request, *args, **kwarg):
        return self.create(request, *args, **kwarg)
    
    def put(self, request, *args, **kwarg):
        return self.update(request, *args, **kwarg)
    
    def patch(self, request, *args, **kwarg):
        return self.partial_update(request, *args, **kwarg)
    