# Generated by Django 4.0.3 on 2022-03-25 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'ordering': ['id'], 'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='questions',
            options={'ordering': ['id'], 'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='quizzes',
            options={'ordering': ['id'], 'verbose_name': 'Тест', 'verbose_name_plural': 'Тесты'},
        ),
        migrations.RemoveField(
            model_name='questions',
            name='difficulty',
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_text',
            field=models.CharField(max_length=255, verbose_name='Текст ответа'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='is_right',
            field=models.BooleanField(default=False, verbose_name='Правильный ответ'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='quiz.questions', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Последнее обновление'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активный статус'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='question', to='quiz.quizzes', verbose_name='Тест'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='quizzes',
            name='title',
            field=models.CharField(default='Новый тест', max_length=255, verbose_name='Название теста'),
        ),
    ]
