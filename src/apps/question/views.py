from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.answer.serializers import AnswerSerializer
from apps.question.models import Question
from apps.question.serializers import QuestionSerializer


class QuestionViewSet(ModelViewSet):
    http_method_names = ["get", "post", "delete"]
    queryset = Question.objects.prefetch_related("answers").order_by("-created_at")
    serializer_class = QuestionSerializer

    @action(detail=True, methods=["post"], url_path="answers")
    def create_answer(self, request, pk=None):
        question = self.get_object()
        serializer = AnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(question=question, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
