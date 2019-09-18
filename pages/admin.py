from django.contrib import admin
from .models import Pages

class PagesAdmin(admin.ModelAdmin):
	fields = ( 'title', 'slug', 'meta_title' )
	list_display = ( 'title', 'slug' )

admin.site.register( Pages, PagesAdmin )
