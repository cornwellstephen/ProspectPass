from django.conf.urls import url
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
urlpatterns = router.urls # note that this fucks up the above url patterns, testing just for angular
