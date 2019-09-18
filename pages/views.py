from django.http import Http404
from django.shortcuts import render
from django.views import View
from .models import Pages

# Create your views here.
class PagesView(View):

	def get(self, request, *arg, **kwargs):
		try:
			page = Pages.objects.get(slug=self.kwargs.get('slug'))
			return render(request, 'page.html', { 'page': page } )

		except Pages.DoesNotExist:
			raise Http404('Page does not exists.')
		return render(request, 'index.html', { 'page': Pages.objects.get(is_home=True) } )


