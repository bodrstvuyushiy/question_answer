from rest_framework import serializers

from apps.answer.serializers import AnswerSerializer
from apps.question.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ("id", "text", "created_at", "answers")
        read_only_fields = ("id", "created_at", "answers")

    def get_answers(self, obj: Question):
        serializer = AnswerSerializer(obj.answers.all(), many=True)  # type: ignore
        return serializer.data
