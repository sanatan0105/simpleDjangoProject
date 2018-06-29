
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^gst/action_page', views.add_product, name='add_product'),
]


