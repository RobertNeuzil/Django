from django.db import models

# Create your models here.

class Poll(models.Model):
	text = models.CharField(max_length=255)
	pub_date = models.DateField()

	def __str__(self):
		return f'{self.text[:50]}'

class Choice(models.Model):
	'''
	The many to one relationship ties the choices to the poll with the question variable

	https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_one/
	'''
	question = models.ForeignKey(Poll, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=255)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return f'{self.choice_text}'  