from django.contrib import admin
from .models import Topic,Link

admin.site.register(Link)


class LinkInline(admin.StackedInline):
	model = Link
	extra = 1

class TopicAdmin(admin.ModelAdmin):
	inlines = [
		LinkInline
	]


admin.site.register(Topic, TopicAdmin)
