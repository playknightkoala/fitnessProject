from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('Home.urls')),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]
