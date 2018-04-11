from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from passes import views
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from passes.views import StudentViewSet

router = DefaultRouter()
router.register(prefix="students", viewset=StudentViewSet)


# urlpatterns = [
# 	url(r'^$', views.Index.as_view(), name = 'index'),
# 	url(r'^homepage/$', views.Homepage.as_view(), name = 'homepage'),
# ]
urlpatterns = [
<<<<<<< HEAD
	url(r'^$', views.Index.as_view(), name = 'index'),
	url(r'^homepage/$', views.Homepage.as_view(), name = 'homepage'),
	url(r'^restapi/', include(router.urls)),
=======
	url(r'^', include(router.urls)),
>>>>>>> 276740a2075c293a09853272c9e7fea5506dbf46
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
