from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms import views

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', views.show, name="Página principal"),
                       url(r'(.+)', views.entry, name="Página de la entrada"),
                       )
