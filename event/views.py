from cal.models import EntryItem
from content.generic.views import GenericObjectList, GenericObjectDetail
from content.models import ModelBase
from show.models import Event

class EventEntryItemList(GenericObjectList):
    def get_extra_context(self, *args, **kwargs):
        extra_context = super(EventEntryItemList, self).get_extra_context(*args, **kwargs)
        added_context = {'title': 'Events'}
        if extra_context:
            extra_context.update(
                added_context,
            )
        else:
            extra_context = added_context

        return extra_context
    
    def get_template_name(self):
        return 'event/event_entryitem_list.html'
    
    def get_pagemenu(self, request, queryset):
        return None
    
    def get_queryset(self):
        return EntryItem.permitted.by_model(Event).order_by('start')

event_entryitem_list = EventEntryItemList()

class ObjectDetail(GenericObjectDetail):
    def get_extra_context(self, slug, *args, **kwargs):
        extra_context = super(ObjectDetail, self).get_extra_context(*args, **kwargs)
        added_context = {
            'title': 'Events',
        }
        if extra_context:
            extra_context.update(
                added_context,
            )
        else:
            extra_context = added_context

        return extra_context
   
    def get_template_name(self):
        return 'event/event_detail.html'
    
    def get_pagemenu(self, request, queryset):
        return None

    def get_queryset(self, slug):
        return Event.permitted.all()
    
    def get_url_callable(self):
        return RadioShowContributorURL()

event_object_detail = ObjectDetail()
