from django.db import models
from django.utils.text import slugify

import re

# Create your models here.
# Pages
class Pages(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(blank=True)
	is_home = models.BooleanField('Homepage?', default=False)
	meta_title = models.CharField('Title (meta)', max_length=100, blank=True)
	meta_description = models.CharField('Description (meta)', max_length=250, blank=True)

	class Meta:
		verbose_name_plural = "Pages"

	def save(self, *args, **kwargs):
		# Auto generate slug from title
		if self.slug:
			slug = self.slug
		else:
			slug = slugify(self.title)
		# Add numbering to slug if exists
		similar_name = Pages.objects.filter(slug=slug)
		similar_name = similar_name.exclude(pk=self.pk)
		if similar_name.count() > 0:
			count = Pages.objects.filter(slug__startswith=slug+'-').count() + 1
			slug = slug + '-' + str(count)

		# Auto generate the meta from title
		if not self.meta_title:
			self.meta_title = self.title

		# There will be only one home
		if self.is_home:
			other_home = Pages.objects.filter(is_home=True)
			other_home.update(is_home=False)

		# Saving the models
		self.slug = slug
		super(Pages, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

