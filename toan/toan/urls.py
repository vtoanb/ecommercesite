from django.conf.urls import include, url
from django.contrib import admin
from oscar.app import application
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns
from apps.sitemaps import base_sitemaps

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    url(r'^admin/', include(admin.site.urls)),
    # url(r'i18n/',include('django.conf.urls.i18n')),
    # include basic sitemap
    url(r'^sitemap\.xml$','django.contrib.sitemaps.views.index',{
        'sitemaps':base_sitemaps}),
    url(r'sitemap-(?P<section>.+)\.xml$',
        'django.contrib.sitemaps.views.sitemap',{'sitemaps':base_sitemaps}),
    url(r'', include(application.urls)),

]

# ... your normal urlpatterns here

if settings.DEBUG:
    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
# (r'(?:.*?/)?(?P<path>(css|jquery|jscripts|images)/.+)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
