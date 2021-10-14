from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
    def question_validation(self):
        """
        Check the Question End's wiht ? or not
        """
        if self.question_text[-1] == '?':  
            return True
        return False
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='set_choice')
    choice_text = models.CharField(max_length=50)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text
    