"""bikefit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from cadastros.views import PerfilAvaliadorFormView, PerfilAtletaFormView, AvaliacaoPosturalFormView,listaAvaliadores, listaAtletas, AvaliadorDetailView, AtletaDetailView
from django.conf.urls.static import static
from django.conf import settings

from rest_framework import routers
from api.views import PerfilAtletaViewSet

router = routers.DefaultRouter()

router.register(r'api-atleta', PerfilAtletaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^cadastro-avaliador/$', PerfilAvaliadorFormView.as_view(), name='cadastro_avaliador'),
    url(r'^cadastro-atleta/$', PerfilAtletaFormView.as_view(), name='cadastro_atleta'),
    url(r'^novo-postural/(?P<pk>[-\w]+)/$', AvaliacaoPosturalFormView.as_view(), name='avaliacao_postural'),
    url(r'^lista-avaliadores/$', listaAvaliadores),
    url(r'^lista/(?P<pk>[-\w]+)/$', AvaliadorDetailView.as_view(), name='lista'),
    url(r'^lista-atletas/$', listaAtletas),
    url(r'^detalhe-atleta/(?P<pk>[-\w]+)/$', AtletaDetailView.as_view(), name='detalhe-atleta'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)