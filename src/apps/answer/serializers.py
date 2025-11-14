from rest_framework import serializers

from apps.answer.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("id", "question", "user", "text", "created_at")
        read_only_fields = ("id", "question", "user", "created_at")
