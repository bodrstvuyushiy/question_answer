from rest_framework import mixins, viewsets
from rest_framework.exceptions import MethodNotAllowed

from apps.answer.models import Answer
from apps.answer.serializers import AnswerSerializer


class AnswerViewSet(
    mixins.RetrieveModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet
):
    http_method_names = ["get", "delete"]
    queryset = Answer.objects.select_related("question").order_by("-created_at")
    serializer_class = AnswerSerializer

    def list(self, request, *args, **kwargs) -> Exception:
        raise MethodNotAllowed("GET")
