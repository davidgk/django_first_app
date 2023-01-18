from rest_framework.viewsets import ModelViewSet
from post.api.serializers import PostSerializer
from post.models import Post


class ApiPostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()