from django.contrib import admin
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('core.urls')),
    url('session_security/', include('session_security.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
