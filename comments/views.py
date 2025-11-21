from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer
from .utils import analyze_sentiment
from rest_framework.permissions import IsAuthenticated

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        text = serializer.validated_data['text']
        result = analyze_sentiment(text)
        serializer.save(sentiment=result['sentiment'], confidence=result['confidence'])

class CommentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]