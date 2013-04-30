from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
from info.sitemap  import sitemaps

urlpatterns = patterns('',
    #url(r'^$', 'news.views.index'),
    url(r'^$','info.views.index'),
    url(r'^graduate$','info.views.graduate'),
    url(r'^device$','info.views.device'),
    url(r'^instruction$','info.views.instruction'),
    url(r'^grappelli/',include('grappelli.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/',include(admin.site.urls)),
    url(r'^form/$','info.views.process_form'),
)

#if settings.DEBUG:
#    urlpatterns=patterns('',
#                         url(r'^media/(?P<path>.*)$','django.views.static.serve',
#                             {'document_root':settings.MEDIA_ROOT,'show_indexes':True}),
#                         url(r'',include('django.contrib.staticfiles.urls')),
#                         )+urlpatterns
#if settings.DEBUG:
urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT },name='media'),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT },name='static'),
        )
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT )

from django.contrib.staticfiles.urls import  staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()


