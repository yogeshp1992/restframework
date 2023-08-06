from django.shortcuts import render
from .models import Student
from .serializer import Studentserializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin, UpdateModelMixin

class List__(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = Studentserializer
    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)


