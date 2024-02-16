"""
URL configuration for oiltech_knowledge_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from contacts.views import contacts
from index.views import (
    index_page,
    burial_drilling,
    oil_gas_development,
    pipeline_construction,
    geophysical_exploration,
    electro_maintenance,
    industrial_maintenance,
    info_sys_programming,
    automatic_control_systems,
    economics_accounting,
    geology_exploration,
    applied_geodesy,
    about_site,
)
urlpatterns = [
    path('admin', admin.site.urls),
    path('', index_page, name='index'),
    path('about-site', about_site, name='about-site'),
    path('contacts', contacts, name='contacts'),
    path('burial_drilling/', burial_drilling, name='burial_drilling'),
    path('oil_gas_development/', oil_gas_development, name='oil_gas_development'),
    path('pipeline_construction', pipeline_construction, name='pipeline_construction'),
    path('geophysical_exploration/', geophysical_exploration, name='geophysical_exploration'),
    path('electro_maintenance/', electro_maintenance, name='electro_maintenance'),
    path('industrial_maintenance/', industrial_maintenance, name='industrial_maintenance'),
    path('info_sys_programming/', info_sys_programming, name='info_sys_programming'),
    path('automatic_control_systems/', automatic_control_systems, name='automatic_control_systems'),
    path('economics_accounting/', economics_accounting, name='economics_accounting'),
    path('geology_exploration/', geology_exploration, name='geology_exploration'),
    path('applied_geodesy/', applied_geodesy, name='applied_geodesy'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)