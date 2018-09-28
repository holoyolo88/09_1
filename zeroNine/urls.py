from django.conf.urls import url
from . import views
# postlist 변경
# post_list->main
urlpatterns = [

    #url(r'^$', views.lists, name='lists'),
    url(r'^apply_db$', views.apply_db, name='apply_db'),
    url(r'^apply$', views.apply, name='apply'),
    url(r'^cancel$', views.cancel, name='cancel'),
    url(r'^login$', views.login, name='login'),
    url(r'^main$', views.main, name='main'),
    url(r'^join$', views.join, name='join'),
    url(r'^order$', views.order, name='order'),
    url(r'^participant$', views.participant, name='participant'),
    url(r'^productpage_db$', views.productpage_db, name='productpage_db'),
    url(r'^productpage$', views.productpage, name='productpage'),
    url(r'^registration$', views.registration, name='registration'),
    url(r'^join_db$', views.join_db, name='join_db')
]

