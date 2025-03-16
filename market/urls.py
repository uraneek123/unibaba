"""
URL configuration for market project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

#sussy way to get images to load on website, apparently shouldnt do this on production
from django.conf import settings
from django.conf.urls.static import static

from base.views import index, contact
from rating.views import rate_image

urlpatterns = [
    path('', include('base.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
    path('rating/', include('rating.urls')),
    path('rate/', rate_image, name='rate-view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #also part of the sussy way to get images to load
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)