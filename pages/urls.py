from django.contrib import admin
from django.urls import include, path
from .views import PagesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PagesView.as_view(), name='index' ),
	path('<str:slug>', PagesView.as_view(), name='pages' ),
]
