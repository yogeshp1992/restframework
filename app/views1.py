from .serializer import Studentserializer
from rest_framework import viewsets
from .models import Student

class Student_viewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserializer

