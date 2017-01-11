from django.contrib import admin
from django.db import models
from . import models as my_models

from pagedown.widgets import AdminPagedownWidget
# Register your models here.

class EntryAdmin(admin.ModelAdmin):
	list_display = ('title', 'created',)
	prepopulated_fields = {"slug": ("title",)}
	search_fields = ('title',)
	formfield_overrides = {
		models.TextField: {'widget': AdminPagedownWidget},
	}


admin.site.register(my_models.Entry, EntryAdmin)
admin.site.register(my_models.Tag)
