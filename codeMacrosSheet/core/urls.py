from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('', include ('apps.user.all_auth.urls')),
    path('', include('apps.user.profile_.urls')),

    path('', include('apps.macros.macros_planner.urls')),
    path('', include ('apps.macros.general_info.urls')),
    path('', include('apps.macros.macros_sheet.urls')),

    path('kcal_statistics/', include('apps.macros_statistics.kcal_statistics.urls')),
    path('macros_statistics/', include('apps.macros_statistics.macros_statistics.urls')),
    path('kcal_chart/', include('apps.macros_statistics.kcal_chart.urls')),
    path('macros_chart/', include('apps.macros_statistics.macros_chart.urls')),
    path('statistics_/', include('apps.macros_statistics.statistics_.urls')),

    path('diet/', include('apps.diet.diet.urls')),
    path('', include ('apps.diet.diet_general_info.urls')),
    path('', include ('apps.diet.meal_general_info.urls')),
    path('', include ('apps.diet.meal.urls')),
    path('', include ('apps.diet.food_options.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)