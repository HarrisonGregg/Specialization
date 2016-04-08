from django.contrib import admin
from .models import Topic,Link,Level,Trajectory

admin.site.register(Link)


class LinkInline(admin.StackedInline):
	model = Link
	extra = 1

class TopicAdmin(admin.ModelAdmin):
	inlines = [
		LinkInline
	]

class TopicInline(admin.StackedInline):
	model = Topic
	extra = 1

class LevelInline(admin.StackedInline):
	model = Level
	inlines = [
		TopicInline
	]
	extra = 1

class TrajectoryAdmin(admin.ModelAdmin):
	inlines = [
		LevelInline
	]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Trajectory, TrajectoryAdmin)
