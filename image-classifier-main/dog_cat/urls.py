from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import home

urlpatterns = [
    path('', home, name='home'),
]

# Add this to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

