from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),

    # Examples:
    url(r'^home/$', 'views.home'),
    # url(r'^icratings/', include('icratings.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #home
    #url(r'^home/$', 'django.contrib.auth.views.home', {'template_name': 'home.html'}),
    #login
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),

    #logout
    #url(r'^logout/$', auth_views.logout, {'next_page': '/home/'}, name='logout'),
    
    #quiz url
    url(r'^quiz/', include('quiz.urls')),
    
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


