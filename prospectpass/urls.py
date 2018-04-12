"""prospectpass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# from rest_framework_nested import routers
from passes.views import StudentViewSet
import django_cas_ng.views

# router = routers.SimpleRouter()
# router.register(r'students',StudentViewSet)

urlpatterns = [
	# url(r'^api/v1/', include(router.urls)),
    
	url(r'^', include('passes.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'login/$', django_cas_ng.views.login, name='cas_ng_login'),
    url(r'logout/$', django_cas_ng.views.logout, name='cas_ng_logout'),
]
