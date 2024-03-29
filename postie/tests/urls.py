from django.conf import settings
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('postie.integrations.tilda.urls'))
]

if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    )
