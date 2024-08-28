from rest_framework import serializers
from .models import Product, Category, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    # brand = BrandSerializer()
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = ["name", "brand", "category"]
        # depth = 3


# class PostsModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PostsModel
#         fields = [
#             "id",
#             "title",
#             "description",
#             "author",
#             "created_at",
#             "updated_at",
#             "image",
#             "post_detail",
#         ]

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         if instance.image:
#             representation["image"] = instance.image.name
#         return representation

#     post_detail = serializers.HyperlinkedIdentityField(
#         view_name="postsapi:post", lookup_field="pk"
# )
