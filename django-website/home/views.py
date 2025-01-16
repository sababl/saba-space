from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Home
from .serializers import HomeSerializer

class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    
    def list(self, request):
        # Get the first home object since we only need one instance
        home = self.get_queryset().first()
        if home:
            serializer = self.get_serializer(home)
            return Response(serializer.data)
        return Response({})
