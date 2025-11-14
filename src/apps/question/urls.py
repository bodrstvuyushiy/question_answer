from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.question.views import QuestionViewSet


router = DefaultRouter()
router.register("", QuestionViewSet, basename="questions")

urlpatterns = [
    path("", include(router.urls)),
]
