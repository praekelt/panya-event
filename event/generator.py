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
    for i in range(0, EVENT_COUNT + 1):
        start_date = datetime.now() + timedelta(days=random.randint(1, 30))
        end_date = start_date + timedelta(hours=random.randint(1, 48))
        objects.append({
            "model": "cal.Entry",
            "fields": {
                "start": str(start_date),
                "end": str(end_date),
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
                        "image": random.sample(IMAGES, 1)[0],
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
