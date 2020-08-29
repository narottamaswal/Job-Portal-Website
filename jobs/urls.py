"""jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()
# And include this URLpattern...

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include("accounts.urls")),
   # path(r'report_builder/', include('report_builder.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)