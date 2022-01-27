from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts urls
    path('', include('accounts.urls')),
    # Invoice urls
    path('', include('invoice.urls')),
]


if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
