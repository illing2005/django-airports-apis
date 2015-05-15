from django.conf.urls import url, patterns
from .views import airport_list

urlpatterns = patterns('',
    url(r'^airports/$', airport_list, name='airport_list'), 
)