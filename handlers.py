from piston.handler import BaseHandler

from bb_dataset.models import *

class RaceHandler(BaseHandler):
    allowed_methods = ('GET', )
    model = Race
    fields = ('name', 'slug', 'use_apoth', 'max_rerolls', 'reroll_cost',  
                ('positions', 
                    ('name', 'cost', 'max_qty', 'ma' 'st', 'ag', 'av', 
                        ('skills', 
                            ('name', ), 
                        ),
                    ),
                ), 
             )

    def read(self, request, race=None):
        if race:
            return Race.objects.get(slug=race)
	return Race.objects.all()
