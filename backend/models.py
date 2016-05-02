from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey

class Comment(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)

	score = models.IntegerField(default=0)
	user = models.ForeignKey(User)
	text = models.TextField()

	# comments = models.ManyToManyField(Comment, blank=True, null=True)

class Topic(models.Model):
	name = models.CharField(max_length=100)
	comments = models.ManyToManyField(Comment, blank=True)

	def __str__(self):
		return self.name

	def count_links(self):
		return Link.objects.filter(topic=self).count()

class Link(models.Model):
	topic = models.ForeignKey(Topic, related_name='link') 
	title = models.CharField(max_length=1000)
	url = models.URLField(max_length=1000)
	score = models.IntegerField(default=0)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{topic} - {title}".format(topic=self.topic,title=self.title)

class VocabWord(models.Model):
	date_added = models.DateTimeField(auto_now_add=True)

	topic = models.ForeignKey(Topic, related_name='vocab_word') 
	term = models.CharField(max_length=1000)
	definition = models.TextField()
	score = models.IntegerField(default=0)

	def __str__(self):
		return self.term

class Trajectory(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Level(models.Model):
	trajectory = models.ForeignKey(Trajectory,related_name='levels')
	name = models.CharField(max_length=100)
	topics = models.ManyToManyField(Topic, blank=True)

	def __str__(self):
		return self.name
