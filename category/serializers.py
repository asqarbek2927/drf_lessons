from rest_framework import serializers
from category.models import Category

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title'
        ]

# class CategoryCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = [
#             'title'
#         ]


class CategoryCreateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)

    # def create(self, validated_data):
    #     print(validated_data)
    #     title = self.validated_data.get("title")
    #     # title = self.validated_data["title"]
    #     return Category(
    #         title=title
    #     )
    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        return instance

    def validate_title(self, attr):
        if len(attr) <= 4:
            return serializers.ValidationError("Cateogry yaratish uchun kamida 4 ta harfdan katta uzunlik bolishi kerak!!!")

        return attr

