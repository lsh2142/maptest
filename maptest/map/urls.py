from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.upload_file, name='upload_file'),
    url(r'test',views.test, name='test'),
    url(r'getMarkerData',views.getMarkerData, name='getMarkerData'),
]
