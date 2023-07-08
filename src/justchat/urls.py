from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from chat.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls', namespace='chat')),
    path('accounts/', include("allauth.urls")),
    path("accounts/", include("accounts.urls", namespace='accounts')),
    path('api/', include('api.urls')),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
