from django.conf.urls.defaults import *

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Enable admin.
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Include URLS from the courses app.
    (r'^', include('study2.urls')),
)
