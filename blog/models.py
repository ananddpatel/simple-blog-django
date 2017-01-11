from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Tag(models.Model):
	slug = models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.slug

class EntryQuerySet(models.QuerySet):

	def published(self):
		return self.filter(publish=True)


class Entry(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField(max_length=25000)
	slug = models.SlugField(max_length=200, unique=True)
	publish = models.BooleanField(default=True)
	# auto_now_add makes it so the datetime is added right as the entry is created
	created = models.DateTimeField(auto_now_add=True)
	# auto_now tracks the time when this field is changed
	modified = models.DateTimeField(auto_now=True)
	objects = EntryQuerySet.as_manager()
	tag = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("entry_detail", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = "Blog Entry"
		verbose_name_plural = "Blog Entries"
		ordering = ["-created"] # orders it in reverse created order
