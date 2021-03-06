"""predictlybot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from predictlybot import views

urlpatterns = [
  url( r'^admin/', admin.site.urls ),
  url( r'^api/', include( 'api.urls' ) ),
  url( r'^stories/', include( 'stories.urls' ) ),
  url( r'^help/', views.help_view, name='help_view' ),
  url( r'^about/', views.about_view, name='about_view' ),
  url( r'^', include( 'dashboard.urls' ) ),
] + static( settings.STATIC_URL, document_root=settings.STATIC_ROOT )
