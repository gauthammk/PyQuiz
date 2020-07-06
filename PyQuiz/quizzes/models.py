from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    users = models.ManyToManyField(User)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=True)
    start_time = models.DateTimeField(blank=True, auto_now_add=True)
    end_time = models.DateTimeField(blank=True)
    is_live = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name='questions', null=True, blank=True, default=None)
    text = models.CharField(max_length=500)
    image_url = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers', null=True, blank=True, default=None)
    text = models.TextField(max_length=1000)
    is_correct = models.BooleanField(default=False)


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, blank=True)
    text = models.CharField(max_length=1000, blank=True)
