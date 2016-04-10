from __future__ import unicode_literals

from django.db import models

import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible

# NOTES FOR MOHIT REFERENCE
# create models here to be used for db schema while migrations
# Each model is represented by a class that subclasses django.db.models.Model
# Each model has a number of class variables, each of which represents a database field in the model.
# Each field is represented by an instance of a Field class eg CharField for character fields and DateTimeField for datetimes. This tells Django what type of data each field holds.
# Each field instance will be used as db column name(s)


# use: python manage.py makemigrations polls to tell django that you have made some changes in the models




@python_2_unicode_compatible
class Question(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published') #designate a human readable name
	total_responses = models.IntegerField(default=0)
	def __str__(self):
		return self.question

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

@python_2_unicode_compatible
class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE) #relate to question as foreign key
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text
