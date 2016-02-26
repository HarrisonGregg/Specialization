from django.db import models

class Topic(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Link(models.Model):
	topic = models.ForeignKey(Topic, related_name='topic') 
	title = models.CharField(max_length=1000)
	url = models.URLField(max_length=1000)
	score = models.IntegerField(default=0)

	def __str__(self):
		return "{topic}-{url}".format(topic=self.topic,url=self.url)