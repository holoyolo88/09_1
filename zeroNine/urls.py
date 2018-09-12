from django.conf.urls import url
from . import views
# postlist 변경
# post_list->main
urlpatterns = [

    #url(r'^$', views.lists, name='lists'),
    url(r'^$', views.main, name='main'),
]

