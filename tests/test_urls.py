from http import HTTPStatus

from django.test import TestCase

from polls.models import Poll


class StaticURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.poll = Poll.objects.create(
            title='Лучший покемон', description='Выберите лучшего покемона'
        )

    def test_page_availability_for_user_request_get(self):
        url_pages = [
            '/api/v1/',
            '/api/v1/poll/',
            f'/api/v1/getResult/{StaticURLTests.poll.id}/']

        for url in url_pages:
            with self.subTest(value=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_page_not_availability_for_user_request_get(self):
        url_pages = [
            '/api/v1/createPoll/',
            f'/api/v1/poll/{StaticURLTests.poll.id}/']

        for url in url_pages:
            with self.subTest(value=url):
                response = self.client.get(url)
                self.assertEqual(
                    response.status_code, HTTPStatus.METHOD_NOT_ALLOWED)
