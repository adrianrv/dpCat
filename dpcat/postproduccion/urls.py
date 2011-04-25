from django.conf.urls.defaults import *


urlpatterns = patterns('postproduccion.views',
    url(r'^$', 'index', name ="index"),
    url(r'^crear/$', 'crear', name = "crear"),
    url(r'^crear/(?P<video_id>\d+)/$', 'crear', name = "crear"),
    (r'^fichero_entrada/(?P<video_id>\d+)/$', 'fichero_entrada'),
    (r'^resumen_video/(?P<video_id>\d+)/$', 'resumen_video'),
    (r'^dirlist/$', 'dirlist'),
    url(r'^cola/$', 'cola_base', name = "cola"),
    (r'^cola_listado/$', 'cola_listado'),
    url(r'^mostrar_log/(?P<task_id>\d+)/$', 'mostrar_log', name = "mostrar_log"),
    (r'^definir_metadatos/(?P<tk_str>\w{25})/$', 'definir_metadatos_user'),
    (r'^definir_metadatos/(?P<video_id>\d+)/$', 'definir_metadatos_oper'),
    (r'^aprobacion_video/(?P<tk_str>\w{25})/$', 'aprobacion_video'),
    (r'^rechazar_video/(?P<tk_str>\w{25})/$', 'rechazar_video'),
    (r'^stream/(?P<video_id>\d+).mp4$', 'stream_video'),
    (r'^stream/(?P<tk_str>\w{25}).flv$', 'stream_preview'),
    url(r'^enproceso/$', 'listar_en_proceso', name = "enproceso"),
    url(r'^pendientes/$', 'listar_pendientes', name = "pendientes"),
    url(r'^log/$', 'showlog', name = 'log'),
    url(r'^oldlog/$', 'showlog', { 'old' : True }, name = "oldlog"),
    url(r'^alertas/$', 'alerts', name = "alertas"),
    url(r'^config/$', 'config_settings', name = "config"),
)
