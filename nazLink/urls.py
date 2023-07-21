
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'first.views.error_404'
handler500 = 'first.views.error_500'
handler403 = 'first.views.error_403'
handler400 = 'first.views.error_400'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
