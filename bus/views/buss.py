from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from serializer import Buss, BussSerializer

class BussListCreateView(generics.ListCreateAPIView):
    queryset = Buss.objects.all()
    serializer_class = BussSerializer


class BussDetilView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buss.objects.all()
    serializer_class = BussSerializer
    