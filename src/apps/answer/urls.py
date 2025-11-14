from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.answer.views import AnswerViewSet


router = DefaultRouter()
router.register("", AnswerViewSet, basename="answers")

urlpatterns = [
    path("", include(router.urls)),
]
