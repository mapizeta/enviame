from rest_framework import generics
from rest_framework.response import Response
from .serializer import EmpresaSerializer
from .models import Empresa

class EmpresaCreateApi(generics.CreateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaApi(generics.ListAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaDeleteApi(generics.DestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer