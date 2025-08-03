from rest_framework import serializers
from .models import ActiveOutage,ArchiveOutage

class ActiveOutageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ActiveOutage
        fields='__all__'
class ArchiveOutageSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArchiveOutage
        fields='__all__'

