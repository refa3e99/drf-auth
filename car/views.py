from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .models import Car
from .serializers import CarSerializer
from .permissions import OwnerOnly


# Create your views here.
class CarListCreateView(ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDetailView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [OwnerOnly]