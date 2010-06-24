from django.core.urlresolvers import reverse

from cal.models import EntryItem
from event.models import Event
from panya.generic.views import GenericObjectList, GenericObjectDetail
from panya.models import ModelBase
from panya.view_modifiers import DateFieldIntervalViewModifier

class ObjectList(GenericObjectList):
    def get_extra_context(self, *args, **kwargs):
        return {'title': 'Events'}
    
    def get_view_modifier(self, request, *args, **kwargs):
        return DateFieldIntervalViewModifier(request=request, field_name='start')

    def get_paginate_by(self, *args, **kwargs):
        return 7
    
    def get_queryset(self, *args, **kwargs):
        return EntryItem.permitted.by_model(Event).order_by('start')
    
    def get_template_name(self, *args, **kwargs):
        return 'event/event_entryitem_list.html'

object_list = ObjectList()

class ObjectDetail(GenericObjectDetail):
    def get_extra_context(self, *args, **kwargs):
        return {'title': 'Events'}
    
    def get_view_modifier(self, request, *args, **kwargs):
        return DateFieldIntervalViewModifier(request=request, field_name='start', base_url=reverse("event_entryitem_list"), ignore_defaults=True)

    def get_queryset(self, *args, **kwargs):
        return Event.permitted.all()
        
object_detail = ObjectDetail()
