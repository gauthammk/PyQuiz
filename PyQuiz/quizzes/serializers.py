from rest_framework import serializers
from quizzes.models import Quiz, Question, Answer, Submission


# Answer serialiser
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


# Question serialiser
class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Question
        fields = '__all__'


# Quiz serialiser
class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Quiz
        fields = ['title', 'description', 'end_time', 'users', 'questions']


# Submission serialiser
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
