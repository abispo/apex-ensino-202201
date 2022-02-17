import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data de publicação')

    def __repr__(self):
        return self.question_text

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # pub_date = 2022 2 14 08 00
        # timezone.now() - datetime.timedelta(days=1) = 2022 2 15 08 00
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __repr__(self):
        return self.choice_text

    def __str__(self):
        return self.choice_text
