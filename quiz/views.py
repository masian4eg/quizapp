from django.shortcuts import render
from django.views import generic
from rest_framework import generics
from rest_framework.response import Response

from .models import Quizzes, Questions, Answer
from .serializers import QuizSerializer, QuestionSerializer
from rest_framework.views import APIView


class Quiz(generics.ListAPIView):
    """Вывод списка тестов"""
    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


class QuizQuestion(APIView):
    """Вывод списка тестов по теме с вопросами и ответами"""
    def get(self, request, format=None, **kwargs):
        question = Questions.objects.filter(quiz__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)


