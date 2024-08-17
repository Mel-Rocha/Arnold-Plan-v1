"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('home.urls')),
    path("admin/", admin.site.urls),

    path("", include('theme_material_kit.urls')),

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
    path('', include ('apps.daily_records.urls')),
]
