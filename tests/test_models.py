from django.test import TestCase

from polls.models import Choice, Poll


class PollsModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.poll = Poll.objects.create(
            title='Лучший покемон', description='Выберите лучшего покемона'
        )

    def test_poll_verbose_name(self):
        poll = PollsModelTest.poll
        field_verboses = {
            'title': 'Название голосования',
            'description': 'Описание голосования',
            'pub_date': 'Дата публикации'
        }

        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    poll._meta.get_field(value).verbose_name, expected)

    def test_choice_verbose_name(self):
        choice = Choice.objects.create(
            poll=PollsModelTest.poll, choice_text='Пичу')
        field_verboses = {
            'choice_text': 'Вариант выбора',
            'votes': 'Голоса',
        }

        for value, expected in field_verboses.items():
            with self.subTest(value=value):
                self.assertEqual(
                    choice._meta.get_field(value).verbose_name, expected)

    def test_object_poll_name_is_title_and_choicep_name_is_choice_text(self):
        poll_1 = Poll.objects.get(title=PollsModelTest.poll.title)
        poll_2 = Poll.objects.create(
            title='Лучший покемон 2', description='Выберите лучшего покемона')
        choice = Choice.objects.create(poll=poll_1, choice_text='Пичу')

        str_test = {
            f'{PollsModelTest.poll}': poll_1.title,
            f'{poll_2}': poll_2.title,
            f'{choice}': choice.choice_text
        }

        for value, expected in str_test.items():
            with self.subTest():
                self.assertEqual(value, expected)
