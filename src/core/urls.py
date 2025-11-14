from django.contrib import admin
from django.urls import include, path

api = [
    path("answers/", include("apps.answer.urls")),
    path("questions/", include("apps.question.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(api)),
]
