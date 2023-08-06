from rest_framework import serializers
from app.models import Student

#123
class Studentserializer(serializers.ModelSerializer):

    class Meta:
        model = Student()
        fields = "__all__"

