from .models import Comment
from rest_framework import serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'sentiment', 'confidence', 'created_at']
        read_only_fields = ['sentiment', 'confidence', 'created_at']
