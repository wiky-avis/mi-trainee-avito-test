from django.test import TestCase
from http import HTTPStatus

from polls.models import Poll, Choice


class PollsPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.poll = Poll.objects.create(
            title='Лучший покемон', description='Выберите лучшего покемона'
        )
        cls.choice = Choice.objects.create(poll=cls.poll, choice_text='пичу')

    def test_poll_page_show_correct_context(self):
        response = self.client.get('/api/v1/poll/')

        context = response.json()
        poll_object = context['results']

        self.assertEqual(type(poll_object), list)
        self.assertEqual(poll_object[0]['id'], PollsPagesTests.poll.id)
        self.assertEqual(poll_object[0]['title'], PollsPagesTests.poll.title)
        self.assertEqual(
            poll_object[0]['description'], PollsPagesTests.poll.description)
        self.assertEqual(
            poll_object[0]['pub_date'], str(PollsPagesTests.poll.pub_date))

    def test_getResult_page_show_correct_context(self):
        response = self.client.get(
            f'/api/v1/getResult/{PollsPagesTests.poll.id}/')

        context = response.json()
        poll_choices = context['choices']

        self.assertEqual(context['id'], PollsPagesTests.poll.id)
        self.assertEqual(context['title'], PollsPagesTests.poll.title)
        self.assertEqual(
            context['description'], PollsPagesTests.poll.description)
        self.assertEqual(
            context['pub_date'], str(PollsPagesTests.poll.pub_date))
        self.assertEqual(type(poll_choices), list)
        self.assertEqual(poll_choices[0]['id'], PollsPagesTests.choice.id)
        self.assertEqual(
            poll_choices[0]['choice_text'], PollsPagesTests.choice.choice_text)
        self.assertEqual(
            poll_choices[0]['votes'], PollsPagesTests.choice.votes)

    def test_poll_create(self):
        poll_count = Poll.objects.count()

        data = {}
        response_bad = self.client.post(
            '/api/v1/createPoll/', data=data, content_type='application/json')
        self.assertEqual(response_bad.status_code, HTTPStatus.BAD_REQUEST)

        data = {
            "title": "Какой покемон лучше?",
            "description": "Выберите лучшего покемона",
            "choices": [
                {"choice_text": "пичу"},
                {"choice_text": "черманде"},
                {"choice_text": "минью"}]}
        response = self.client.post(
            '/api/v1/createPoll/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

        test_data = response.json()
        self.assertEqual(type(test_data), dict)

        self.assertEqual(poll_count + 1, Poll.objects.count())

    def test_poll_patch_current_vote(self):
        response = self.client.patch(
            f'/api/v1/poll/{PollsPagesTests.poll.id}/',
            data={"choice_id": 1},
            content_type='application/json')

        self.assertEqual(response.status_code, HTTPStatus.OK)

        test_poll = Choice.objects.filter(id=PollsPagesTests.choice.id).first()
        self.assertEqual(test_poll.votes, 1)
