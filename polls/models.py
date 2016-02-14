from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
	def __str__(self):
		return self.question_text
	question_text = models.CharField(max_length=300)
	pub_date= models.DateTimeField('data published')
	

	
class Choise(models.Model):
	question = models.ForeignKey(Question,on_delete = models.CASCADE)
	choice_text = models.CharField(max_length=200)
	vote = models.IntegerField(default=0)
	
	
	
