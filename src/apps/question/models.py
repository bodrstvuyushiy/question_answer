from django.db import models


class Question(models.Model):
    text = models.TextField(max_length=1028, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        default_related_name = "questions"

    def __str__(self):
        return f"question_id: {self.pk}"
