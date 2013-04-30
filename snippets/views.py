from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from django.contrib.auth.models import User


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format),
        })


class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    model = Snippet
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    model = Snippet
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
            IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class SnippetHighlight(generics.SingleObjectAPIView):
    model = Snippet
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)



class UserList(generics.ListAPIView):
    """
    List all users
    """
    model = User
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve a user instance
    """
    model = User
    serializer_class = UserSerializer
