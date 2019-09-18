from django.contrib import admin
from .models import Pages

class PagesAdmin(admin.ModelAdmin):
	fields = ( 'title', 'slug', 'meta_title', 'meta_description', 'is_home' )
	list_display = ( 'title', 'slug', 'is_home' )

admin.site.register( Pages, PagesAdmin )
