from django.contrib.auth import get_user_model
from django.db import models

from apps.question.models import Question


User = get_user_model()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1028, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        default_related_name = "answers"

    def __str__(self):
        return f"answer_id:{self.pk} | {self.user}"
