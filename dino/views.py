from dino.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import DinoSerializer
from .models import Dino

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Dino.objects.all()
    serializer_class = DinoSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Dino.objects.all()
    serializer_class = DinoSerializer
