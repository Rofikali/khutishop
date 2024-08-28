from .serializers import ProductSerializer, BrandSerializer, CategorySerializer
from .models import Product, Category, Brand

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework import viewsets


class BrandView(viewsets.ViewSet):
    """
    A simple ViewSet for listing all products.
    """

    queryset = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class CategoryView(viewsets.ViewSet):
    """
    A simple ViewSet for listing all products.
    """

    # def get_queryset(self):
    #     return Category.objects.all()

    queryset = Category.objects.all()

    def list(self, request):
        paginator = LimitOffsetPagination()
        paginator.default_limit = 5
        paginator_queryset = paginator.paginate_queryset(self.queryset, request)

        serializer = CategorySerializer(paginator_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)


class CustomPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 50


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters


class CustomPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 50


from rest_framework import viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework import status


class CustomPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 50


# from rest_framework import status


class ProductView(viewsets.ViewSet):
    """
    A simple ViewSet for listing all products.
    """

    queryset = Product.objects.all()
    # Lookup_fields = "name"

    """
    # def list(self, request):
    #     # Set up pagination
    #     paginator = PageNumberPagination()
    #     paginator.page_size = 3

    #     # Apply pagination to the queryset
    #     paginated_queryset = paginator.paginate_queryset(self.queryset, request)

    #     # Serialize the paginated data
    #     serializer = ProductSerializer(paginated_queryset, many=True)
    #     # return Response(serializer.data)
    #     # Return the paginated response
    #     return paginator.get_paginated_response(serializer.data)
    """

    def list(self, request):
        # Set up pagination
        paginator = LimitOffsetPagination()
        paginator.default_limit = 5
        # Apply pagination to the queryset
        paginated_queryset = paginator.paginate_queryset(self.queryset, request)
        print("request ", request)
        # Serialize the paginated data
        serializer = ProductSerializer(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def retrieve(self, request, pk=None):

        queryset = Product.objects.filter(category__name=pk)
        print(request,'data ')
        print(request,'data bane;m ', pk)
        # singe_data = get_object_or_404(queryset, name=name)
        try:
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)
        except:
            serializer = ProductSerializer(queryset)
            return Response(serializer.error)

    # def retrieve(self, request, pk=None):
    #     singe_data = get_object_or_404(self.queryset, pk=pk)
    #     try:
    #         serializer = ProductSerializer(singe_data)
    #         return Response(serializer.data)
    #     except Exception as e:
    #         serializer = ProductSerializer(singe_data)
    #         return Response(serializer.error, status=status)
