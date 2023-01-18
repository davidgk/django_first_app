from rest_framework.routers import DefaultRouter

from post.api.views import ApiPostViewSet

router_posts = DefaultRouter()
router_posts.register(prefix='post', basename='post', viewset=ApiPostViewSet)
