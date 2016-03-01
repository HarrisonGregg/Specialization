from django.test import TestCase, Client
from .models import Topic,Link
import json

# Create your tests here.
class TestSuite(TestCase):
	def setUp(self):
		self.topic = Topic(name="MyTopic")
		self.topic.save()
		self.c = Client()

	def testTopics(self):
		"""Test Topics"""
		topics = Topic.objects.all()
		self.assertGreater(len(topics), 0)

		Topic.objects.create(name="TopicToDelete")
		myTopic = Topic.objects.get(name="TopicToDelete")
		self.assertIsNotNone(myTopic)
		topic = Topic.objects.get(name="TopicToDelete")
		topic.delete()

		topics = Topic.objects.filter(name="TopicToDelete")
		self.assertEqual(len(topics),0)

	def testLinks(self):
		"""Test Links"""
		link = Link(topic=self.topic,title="Link Title",url="Link URL")
		link.save()
		links = Link.objects.filter(topic__name="MyTopic")
		self.assertGreater(len(links),0)
		link.score = 1
		link.save()

		link = Link.objects.get(title="Link Title")
		self.assertEqual(link.score,1)
		link.delete()

		links = Link.objects.filter(title="Link Title")
		self.assertEqual(len(links),0)

	def testTopicRequests(self):
		"""Test Topics Requests"""
		response = self.c.get('/topics/')
		self.assertEqual(response.status_code, 200)
		topics = response.json()
		self.assertGreater(len(topics),0)

		response = self.c.post('/topics/', {'name': 'TopicToDelete'})
		self.assertEqual(response.status_code, 201)
		topic = response.json()
		self.c.delete('/topics/{0}/'.format(topic['pk']))

		response = self.c.get('/topics/{0}/'.format(topic['pk']))
		self.assertEqual(response.status_code, 404)

	def testLinkRequests(self):
		"""Test Links Requests"""
		response = self.c.get('/links/')
		self.assertEqual(response.status_code, 200)

		response = self.c.post('/links/',data={"topic":self.topic.id,"title":"Link Title","url":"http://wikipedia.com/Topic"})
		self.assertEqual(response.status_code, 201)
		link = response.json()
		self.assertEqual(link['title'],"Link Title")

		response = self.c.get('/links/')
		self.assertEqual(response.status_code, 200)
		links = response.json()
		self.assertGreater(len(links),0)
		link['score'] = 1
		response = self.c.put('/links/{0}/'.format(link['pk']),data=json.dumps(link),content_type='application/json')
		self.assertEqual(response.status_code, 200)

		response = self.c.get('/links/{0}/'.format(link['pk']))
		self.assertEqual(response.status_code, 200)
		link = response.json()
		self.assertEqual(link["score"],1)
		response = self.c.delete('/links/{0}/'.format(link['pk']))
		self.assertEqual(response.status_code, 204)

		response = self.c.get('/links/{0}/'.format(link['pk']))
		self.assertEqual(response.status_code, 404)





