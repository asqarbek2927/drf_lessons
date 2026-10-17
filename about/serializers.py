from rest_framework import serializers

from about.models import About


class AboutListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()

class AboutCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()

    def create(self, validated_data):
        return About.objects.create(**validated_data)

