from django.db import models


# Create your models here.
class Answer(models.Model):
    answer = models.CharField(max_length=255)


class Question(models.Model):
    question = models.CharField(max_length=255)


class QuestionsAnswers(models.Model):
    question_id = models.IntegerField()
    answer_id = models.IntegerField(primary_key=True)
    correct = models.BooleanField()


class Statistics(models.Model):
    question = models.OneToOneField(Question,
                                    on_delete=models.CASCADE,
                                    primary_key=True)
    answered_time = models.IntegerField()
    right_answered_time = models.IntegerField()
