import serializers as serializers
from rest_framework import serializers


class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField()
