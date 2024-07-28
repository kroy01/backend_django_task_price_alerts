from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache
from .models import Alert
from .serializers import AlertSerializer
from .permissions import IsOwner


class AlertCreateView(generics.CreateAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlertDeleteView(generics.DestroyAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)


class AlertListView(generics.ListAPIView):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('status',)

    def get_queryset(self):
        user = self.request.user
        return Alert.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        user = request.user
        cache_key = f'alerts_{user.id}'
        alerts = cache.get(cache_key)

        if not alerts:
            queryset = self.filter_queryset(self.get_queryset())
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                cache.set(cache_key, serializer.data, timeout=60 * 15)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            cache.set(cache_key, serializer.data, timeout=60 * 15)
            return Response(serializer.data)

        return Response(alerts)
