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

    def validate(self, attrs):
        name = attrs.get("name")
        price = attrs.get("price")
        description = attrs.get("description")

        if len(name) <= 4:
            raise serializers.ValidationError("Name 4ta harfdan uzunroq bolishi kerak")

        if price <= 999:
            raise serializers.ValidationError("Minimum 1000 som bolishi kerak narxi producti!!!")

        if len(description) < 39:
            raise serializers.ValidationError("Produtiz haqida koproq informatsiya yozing!!!")
        return attrs

