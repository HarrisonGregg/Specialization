from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey

# class Comment(models.Model):
# 	parent = GenericForeignKey()
# 	user = ForeignKey(User)
# 	text = models.TextField()
# 	date_created = models.DateTimeField(auto_now_add=True)

class Topic(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	def count_links(self):
		return Link.objects.filter(topic=self).count()

class Link(models.Model):
	topic = models.ForeignKey(Topic, related_name='topic') 
	title = models.CharField(max_length=1000)
	url = models.URLField(max_length=1000)
	score = models.IntegerField(default=0)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{topic} - {title}".format(topic=self.topic,title=self.title)

class VocabWord(models.Model):
	date_added = models.DateTimeField(auto_now_add=True)
	
	topic = models.ForeignKey(Topic, related_name='topic') 
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
