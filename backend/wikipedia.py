from wikiapi import WikiApi
from .models import Link, Topic

def wiki_api(options):
	wiki = WikiApi()
	wiki = WikiApi({ 'locale' : 'en'}) # to specify your locale, 'en' is default
	results = wiki.find(options['q'])
	for result in results:
		article = wiki.get_article(results)
		title = article.heading
		url = article.url

		print(url)
		link = Link(topic = options['topic'], title = title, url = url)
		link.save()
