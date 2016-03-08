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
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{topic} - {title}".format(topic=self.topic,title=self.title)