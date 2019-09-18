from django.db import models
from django.utils.text import slugify

import re

# Create your models here.
# Pages
class Pages(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(blank=True)
	meta_title = models.CharField('Title (meta)' max_length=100, blank=True)
	meta_description = models.CharField('Description (meta)', max_length=250, blank=True)

	def save(self, *args, **kwargs):
		# Auto generate slug from title
		if self.slug:
			slug = self.slug
		else:
			slug = slugify(self.title)
		# Add numbering to slug if exists
		similar_name = Pages.objects.filter(slug__startswith=slug)
		if similar_name.count() > 0:
			slug = slug + '-' + str(similar_name.count())

		# Auto generate the meta from title
		if not self.meta_title:
			self.meta_title = self.title

		# Saving the models
		self.slug = slug
		super(Pages, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

