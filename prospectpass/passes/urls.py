from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from passes import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.Index.as_view(), name = 'index'),
	url(r'^homepage/$', views.Homepage.as_view(), name = 'homepage')
]
urlpatterns = format_suffix_patterns(urlpatterns)