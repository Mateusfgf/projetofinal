from django.conf.urls import url
from . import views

urlpatterns = [
	    url(r'^$', views.listar_postagem, name='listar_postagem'),
	    url(r'^postagem/(?P<pk>\d+)/$', views.detalhando_postagem, name='detalhando_postagem')
]