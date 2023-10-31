from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from ..serializer import Buss, BussSerializer, Route, RouteSerializer
from rest_framework import filters


class BussListCreateView(generics.ListCreateAPIView):
    queryset = Buss.objects.all()
    serializer_class = BussSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['busnumber',]


class BussDetilView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Buss.objects.all()
    serializer_class = BussSerializer

    def retrieve(self, request, *args, **kwargs):
        buss_obj = Buss.objects.get(pk = kwargs['pk'])
        buss = BussSerializer(buss_obj).data

        route_obj = Route.objects.get(buss = buss['id'])
        route = RouteSerializer(route_obj, many = False).data

        data = {
            'buss':buss,
            'route':route,
        }
        return Response(data=data)
