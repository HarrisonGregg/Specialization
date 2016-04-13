from django.db import models

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

class Trajectory(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Level(models.Model):
	trajectory = models.ForeignKey(Trajectory,related_name='levels')
	name = models.CharField(max_length=100)
	topics = models.ManyToManyField(Topic)

	def __str__(self):
		return self.name
