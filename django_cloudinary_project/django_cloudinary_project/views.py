from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
@renderer_classes([JSONRenderer, BrowsableAPIRenderer])
def api_root(request, format=None):
    return Response({
        'posts': reverse('post-list', request=request, format=format),
        'comments': reverse('comment-list', request=request, format=format),
        'profiles': reverse('profile-list', request=request, format=format),
        'likes': reverse('like-list', request=request, format=format),
        'followers': reverse('follower-list', request=request, format=format),
    })