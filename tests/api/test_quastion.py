import pytest
from apps.answer.serializers import AnswerSerializer
from apps.answer.models import Answer
from apps.question.models import Question


pytestmark = pytest.mark.django_db


def test_get_questions(api_client):
    client = api_client
    question = Question.objects.create(text="Почему, мистер Андерсон, почему?")
    url = "/questions/"
    expected_status_code = 200

    response = client.get(url)  # act
    payload = response.json()

    assert response.status_code == expected_status_code
    assert payload[0]["text"] == question.text


def test_create_question(api_client):
    client = api_client
    url = "/questions/"
    text = "Во имя чего? Что вы делаете?"
    expected_status_code = 201

    response = client.post(url, {"text": text}, format="json")  # act
    payload = response.json()

    assert response.status_code == expected_status_code
    assert payload["text"] == text


def test_get_questions_id(api_client):
    client = api_client
    question = Question.objects.create(
        text="""Зачем, зачем встаете? Зачем продолжаете драться? 
                                               Неужели вы верите в какую-то миссию, 
                                               или вам просто страшно погибать?"""
    )
    url = f"/questions/{question.pk}/"
    expected_answers = AnswerSerializer(
        Answer.objects.filter(question=question), many=True
    ).data
    expected_status_code = 200

    response = client.get(url)  # act
    payload = response.json()

    assert response.status_code == expected_status_code
    assert payload["id"] == question.pk
    assert payload["text"] == question.text
    assert payload["answers"] == expected_answers


def test_delete_question(api_client):
    client = api_client
    question = Question.objects.create(
        text="Так в чем же миссия, может быть, вы откроете?"
    )
    url = f"/questions/{question.pk}/"
    expected_status_code = 204

    response = client.delete(url)  # act

    assert response.status_code == expected_status_code
    assert not Question.objects.filter(pk=question.pk).exists()
