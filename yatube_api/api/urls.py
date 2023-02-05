from rest_framework.routers import SimpleRouter
from django.urls import path, include

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = SimpleRouter()

version = 'v1/'

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register('follow', FollowViewSet)

urlpatterns = [
    path(version + '', include(router.urls)),
    path(version + 'follow/', FollowViewSet),
    path(version, include('djoser.urls')),
    path(version, include('djoser.urls.jwt')),
]
