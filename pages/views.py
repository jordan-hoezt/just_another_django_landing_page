from django.http import Http404
from django.shortcuts import render
from django.views import View
from .models import Pages

# Create your views here.
class PagesView(View):

	def get(self, request, *arg, **kwargs):
		if self.kwargs.get('slug'):
			try:
				page = Pages.objects.get(slug=self.kwargs.get('slug'))
				return render(request, 'page.html', { 'page': page } )
			except Pages.DoesNotExist:
				raise Http404('Page does not exists.')
		else:
			return render(request, 'index.html', { 'page': Pages.objects.get(is_home=True) } )


