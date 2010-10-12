from django.conf.urls.defaults import *
from piston.resource import Resource
from bb_dataset.handlers import RaceHandler

race_resource = Resource(handler=RaceHandler)

urlpatterns = patterns('',
   (r'race/$', race_resource),
   (r'race/(?P<race>)/$', race_resource),
)
