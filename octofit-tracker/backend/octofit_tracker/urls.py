from django.contrib import admin
from django.urls import path, include

# Az URL útvonalak listája
VAR_URL_PATTERNS = [
    path('admin/', admin.site.urls),
    # Ez a sor engedélyezi a REST API bejelentkezési felületét
    path('api-auth/', include('rest_framework.urls')),
]

# Átadjuk a Django-nak a változót
urlpatterns = VAR_URL_PATTERNS