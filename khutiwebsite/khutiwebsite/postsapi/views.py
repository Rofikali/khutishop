from rest_framework.generics import ListAPIView, RetrieveAPIView


from .models import PostsModel
from .serializers import PostsModelSerializer


class PostsListAPIView(ListAPIView):
    queryset = PostsModel.objects.all()
    serializer_class = PostsModelSerializer


class PostsRetrieveAPIView(RetrieveAPIView):
    queryset = PostsModel.objects.all()
    serializer_class = PostsModelSerializer
