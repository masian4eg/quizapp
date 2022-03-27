from django.test import TestCase
from . import models
import logging


logger = logging.getLogger(__name__)


class BaseNotificationsTests(TestCase):
    @staticmethod
    def create_test_fixtures():
        try:
            # создаём тестовые объекты и сохраняем их в БД
            cat1 = models.Category(name='cat1')
            cat1.save()
            cat2 = models.Category(name='cat2')
            cat2.save()

            quiz1 = models.Quizzes(title='quiz1', category=cat1)
            quiz1.save()
            quiz2 = models.Quizzes(title='quiz2', category=cat2)
            quiz2.save()

            q1 = models.Questions(title='q1', quiz=quiz1)
            q1.save()
            q2 = models.Questions(title='q2', quiz=quiz2)
            q2.save()

            models.Answer(answer_text='a1', question=q1, is_right=True).save()
            models.Answer(answer_text='a2', question=q1, is_right=False).save()
            models.Answer(answer_text='a3', question=q2, is_right=True).save()
            models.Answer(answer_text='a4', question=q2, is_right=False).save()

        # если какая-то ошибка - выводим её
        except Exception as e:
            logger.error(f'Ошибка: {e}')

    def test_index_loads(self):
        """Проверяет доступность страницы quiz"""
        response = self.client.get('http://127.0.0.1:8000/quiz/')
        self.assertEqual(response.status_code, 200)

    def test_mailngs_loads(self):
        """Проверяет доступность страницы"""
        # создаём тестовые объекты
        BaseNotificationsTests.create_test_fixtures()

        response = self.client.get('http://127.0.0.1:8000/quiz/')
        self.assertEqual(response.status_code, 200)
