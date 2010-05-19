import random
from datetime import datetime, timedelta

from django.conf import settings

from generate import IMAGES
from generate.json_loader import load_json
from event.models import PROVINCES

EVENT_COUNT = 20

def generate():
    objects = []
    
    # create event, venue and location objects
    for i in range(1, EVENT_COUNT + 1):
        objects.append({
            "model": "event.Event",
            "fields": {
                "title": "Event %s Title" % i,
                "description": "Event %s description with some added text to verify truncates where needed." % i,
                "content": "Event %s Content" % i,
                "state": "published",
                "image": random.sample(IMAGES, 1)[0],
                "sites": {
                    "model": "sites.Site",
                    "fields": { 
                        "name": "example.com",
                    }
                },
                "venue": {
                    "model": "event.Venue",
                    "fields": { 
                        "name": "Venue %s Title" % i,
                        "address": "Venue %s Address" % i,
                        "location": {
                            "model": "event.Location",
                            "fields": {
                                "city": "City %s Title" % i,
                                "province": "%s" % random.choice(PROVINCES)[0],
                            }
                        },
                    }
                },
            },
        })
    
    # create some entries for events
    for i in range(0, 24, 4):
        start_hour = i
        end_hour = 23 if i + 4 == 24 else i + 4
        objects.append({
            "model": "cal.Entry",
            "fields": {
                "start": str(datetime.now().replace(hour=start_hour, minute=0, second=0, microsecond=0)),
                "end": str(datetime.now().replace(hour=end_hour, minute=0, second=0, microsecond=0)),
                "content": {
                    "model": "event.Event",
                    "fields": {
                        "title": "Event %s Title" % random.randint(1, EVENT_COUNT),
                    }
                },
                "calendars": {
                    "model": "cal.Calendar",
                    "fields": {
                        "title": "Calendar 2 Title",
                        "state": "published",
                        "sites": {
                            "model": "sites.Site",
                            "fields": { 
                                "name": "example.com"
                            },
                        },
                    },
                },
            },
        })
    
    load_json(objects)
