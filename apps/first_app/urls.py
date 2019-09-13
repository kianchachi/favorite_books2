from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^login$',views.login),
    url(r'^success$',views.success),
    url(r'^add$',views.add),
    url(r'^show/(?P<show_id>\d+)$', views.edit),
    url(r'^show/(?P<show_id>\d+)/delete$', views.delete),
    url(r'^like/(?P<show_id>\d+)/$', views.like),

    # url(r'^update/(?P<show_id>\d+)$', views.update),

]
