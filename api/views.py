from rest_framework import generics
from .models import Vlog
from .serializers import VlogSerializer

class VlogList(generics.ListCreateAPIView):
    queryset = Vlog.objects.all()
    serializer_class = VlogSerializer

class VlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vlog.objects.all()
    serializer_class = VlogSerializer
