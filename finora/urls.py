from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from core.urls import plain_patterns, site_patterns

admin.site.site_header = 'Finora Systems'
admin.site.site_title = 'Finora admin'
admin.site.index_title = 'Boshqaruv paneli'

urlpatterns = [
    path('admin/', admin.site.urls),
    *plain_patterns,
    # O'zbekcha — prefikssiz (/), inglizcha — /en/, ruscha — /ru/
    *i18n_patterns(*site_patterns, prefix_default_language=False),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'core.views.page_not_found'
