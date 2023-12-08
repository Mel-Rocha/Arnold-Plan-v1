from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include ('all_auth.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('profile_.urls')),
    path('', include('macros_planner.urls')),
    path('', include ('general_info.urls')),
    path('', include('macros_sheet.urls')),
    path('kcal_statistics/', include('kcal_statistics.urls')),
    path('macros_statistics/', include('macros_statistics.urls')),
    path('kcal_chart/', include('kcal_chart.urls')),
    path('macros_chart/', include('macros_chart.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)