from rest_framework import serializers
from product.models import Product


class ProductPostSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()

    # def create(self, validated_data):
    #     name = self.validated_data.get("name")
    #     # name = self.validated_data["name"]
    #     return Product(
    #         name
    #     )
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.price = validated_data.get("price", instance.price)
        instance.description = validated_data.get("description", instance.description)
        instance.save()
        return instance

    def validate_name(self, attr):
        if attr.lower() == "uzum":
            raise serializers.ValidationError(f"Bizda {attr} sozili product yaratish mumkun emas!!!")
        return attr

    def validate_price(self, attr):
        if attr < 999:
            raise serializers.ValidationError(f"Bizda minimum pricelik mahsulot 999som!!!!")
        return attr
    def validate_description(self, attr):
        if len(attr) <= 40:
            raise serializers.ValidationError("Product haqida koproq malumot bering!!!")
        return attr

    # def validate(self, attrs): #qisqa validatelar uchun
    #     title = attrs.get("title")
    #     price = attrs.get("price")
    #     description = attrs.get("description")



class ProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'description'
        ]
        extra_kwargs = {
            'id': {"read_only":True}
        }