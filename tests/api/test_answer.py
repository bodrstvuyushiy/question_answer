import pytest

from apps.answer.models import Answer
from apps.question.models import Question


pytestmark = pytest.mark.django_db


def test_create_answers(user):
    question = Question.objects.create(text="Убить Вас — наслаждение.. ")
    text = "мистер Андерсон."

    answer = Answer.objects.create(text=text, question=question, user=user)  # act

    assert answer.question == question
    assert answer.text == text


def test_get_answer_id(api_client, user):
    client = api_client
    question = Question.objects.create(
        text="""Это свобода, правда, может быть, мир, или вы боретесь за любовь?
                                               Иллюзии, мистер Андерсон, причуды восприятия. 
                                               Хрупкие логические теории слабого человека, который отчаянно пытается оправдать свое существование 
                                               — бесцельное и бессмысленное! Но они, мистер Андерсон, как и Матрица, столь же искусственны. 
                                               Только человек может выдумать скучное и безжизненное понятие — «любовь»! 
                                               Вам пора это увидеть, мистер Андерсон, увидеть и понять! 
                                               Вы не можете победить, продолжать борьбу бессмысленно. 
                                               Почему, мистер Андерсон, почему вы упорствуете?"""
    )
    text = "Потому что это мой выбор"
    answer = Answer.objects.create(text=text, question=question, user=user)
    url = f"/answers/{answer.pk}/"
    expected_status_code = 200

    response = client.get(url)  # act
    payload = response.json()

    assert response.status_code == expected_status_code
    assert payload["id"] == answer.pk
    assert payload["question"] == question.pk
    assert payload["user"] == str(user.pk)
    assert payload["text"] == text


def test_delete_answer(api_client, user):
    cleint = api_client
    question = Question.objects.create(
        text="""Вы слышите, мистер Андерсон? Это — рок, неизбежность. 
                                               Шаги вашей смерти. Прощайте, мистер Андерсон!"""
    )
    answer = Answer.objects.create(
        text="Меня зовут... Нео", question=question, user=user
    )
    url = f"/answers/{answer.pk}/"
    expected_status_code = 204

    response = cleint.delete(url)  # act

    assert response.status_code == expected_status_code
    assert not Answer.objects.filter(pk=question.pk).exists()
