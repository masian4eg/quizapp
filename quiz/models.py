from django.db import models
from rest_framework.authtoken.admin import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.name


class Quizzes(models.Model):
    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'
        ordering = ['id']

    title = models.CharField(max_length=255, default='Новый тест', verbose_name='Название теста')
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name='Последнее обновление', auto_now=True)

    class Meta:
        abstract = True


class Questions(Updated):
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['id']

    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING, verbose_name='Тест')
    title = models.CharField(max_length=255, verbose_name='Название')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title


class Answer(Updated):
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['id']

    question = models.ForeignKey(Questions, related_name='answer', on_delete=models.CASCADE, verbose_name='Вопрос')
    answer_text = models.CharField(max_length=255, verbose_name='Текст ответа')
    is_right = models.BooleanField(default=False, verbose_name='Правильный ответ', blank=False)

    def __str__(self):
        return self.answer_text


class Profile(models.Model):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    result = models.ForeignKey(Answer, verbose_name='Результат', on_delete=models.DO_NOTHING)

    def get_score(self):
        score = 0
        if Answer.is_right:
            score += 1
        return score
