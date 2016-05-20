from django.conf.urls import include, url
from django.contrib import admin
from oscar.app import application
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include(application.urls)),
]

# ... your normal urlpatterns here

if settings.DEBUG:
    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
