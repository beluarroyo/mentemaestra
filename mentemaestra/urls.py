from django.conf.urls import url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    
    url(r'^vista2/', vista2),

    url(r'^vista3/', vista2),
    
    url(r'^admin/', admin.site.urls),



]
