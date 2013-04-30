from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    """
    List all snippets, or create a new snippet.
    """
    model = Snippet
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    model = Snippet
    serializer_class = SnippetSerializer
