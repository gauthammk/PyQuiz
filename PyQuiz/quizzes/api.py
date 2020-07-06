from quizzes.models import Quiz, Question, Answer, Submission
from rest_framework import viewsets, permissions, generics
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer, SubmissionSerializer


# Quiz Viewset for CRUD
class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuizSerializer


# Question Viewset
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuestionSerializer


# Answer Viewset
class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnswerSerializer


# Submission Viewset
class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubmissionSerializer
