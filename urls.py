###########################################################################
#    Copyright (C) 2009 by Stephane Doiron                                      
#    <maddox@rimshot.org>                                                             
#
# Copyright: See COPYING file that comes with this distribution
#
###########################################################################
from django.conf.urls.defaults import *
from bloodbowl.bb_dataset.models import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

race_dict = {
	'queryset': Race.objects.all(),
	'template_name': 'data/race_list.html',
	'template_object_name': 'race',
}

urlpatterns = patterns('',
    # Example:
    # (r'^bloodbowl/', include('bloodbowl.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    #(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    ## Uncomment the next line to enable the admin:
    #(r'^admin/(.*)', admin.site.root),
    #(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    #(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
    #(r'^team/', include('bloodbowl.team_manager.urls')),
    #(r'^race/', include('bloodbowl.bb_dataset.urls')),
    (r'^race/$', 'django.views.generic.list_detail.object_list', race_dict)
)
