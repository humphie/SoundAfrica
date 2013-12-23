from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sound_frica.views.home', name='home'),
    # url(r'^sound_frica/', include('sound_frica.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^register_device/', 'music_distributor.views.register_device', name='register_device'),  # MOBILE HANDLER
    url(r'^login_device/', 'music_distributor.views.login_device', name='login_device'),  # MOBILE HANDLER
    url(r'^logout_device/', 'music_distributor.views.logout_device', name='logout_device'),  # MOBILE HANDLER
    url(r'^request_collection/', 'music_distributor.views.send_collection', name='send_collection'),  # MOBILE HANDLER
    url(r'^request_order/', 'music_distributor.views.receive_order', name='receive_order'),  # MOBILE HANDLER
    url(r'^admin/', include(admin.site.urls)),
)
