from django import template

register = template.Library()

@register.inclusion_tag('event/inclusion_tags/event_entryitem_listing.html')
def event_entryitem_listing(object_list):
    return {'object_list': object_list}

@register.inclusion_tag('event/inclusion_tags/event_detail.html')
def event_detail(obj):
    return {'object': obj}
