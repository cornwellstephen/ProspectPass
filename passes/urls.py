from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from passes import views
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from passes.views import StudentViewSet, PassViewSet

router = DefaultRouter()
router.register(prefix="students", viewset=StudentViewSet)
router.register(prefix="passes", viewset=PassViewSet)


# urlpatterns = [
	# url(r'^$', views.Index.as_view(), name = 'index'),
	# url(r'^homepage/$', views.Homepage.as_view(), name = 'homepage'),
# ]
urlpatterns = [
	url(r'^$', views.Index.as_view(), name = 'index'),
	url(r'^homepage/$', views.Homepage.as_view(), name = 'homepage'),
	url(r'^sendpass/(?P<pk>\d+)/$', views.send_pass, name = 'sendpass'),
    url(r'^admin-homepage/$', views.AdminHomepage.as_view(), name = 'admin-homepage'),
	url(r'^sentpass/$', views.SentPass.as_view(), name = 'sentpass'),
	url(r'^restapi/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace ='rest_framework')),
]
