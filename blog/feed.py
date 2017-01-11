from django.contrib.syndication.views import Feed
from .models import Entry

class LatestPost(Feed):
	title = "My Test Blog"
	link = "/feed/"
	description = "Latest Posts of " + title

	def items(self):
		return Entry.objects.published()[:5]