
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls')),
    path('account/', include('account.urls')),
    path('', include('app_shop.urls')),
    
]

if settings.DEBUG:

    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

import datetime
print(datetime.datetime.now(), __name__)
