from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'event.views',
    url(r'^list/$', 'object_list', name='event_entryitem_list'),
    url(r'^(?P<slug>[\w-]+)/$', 'object_detail', name='event_object_detail'),
)
