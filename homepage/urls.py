from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),        #http://127.0.0.1:8000/homepage/
    path('qwe/', qwe, name='qwe'),      #http://127.0.0.1:8000/homepage/qwe/
    path('docker/', docker, name='docker'),
    path('systemd/', systemd, name='systemd'),
    path('samba/', samba, name='samba'),
    path('disk/', disk, name='disk'),
    path('swap-linux/', swap_linux, name='swap_linux'),
    path('firewalld/', firewalld, name='firewalld'),
    path('cisco/', cisco, name='cisco'),
    path('postgresql/', postgresql, name='postgresql'),
    path('netsh/', netsh, name='netsh'),
    path('haproxy/', haproxy, name='haproxy'),
    path('ufw/', ufw, name='ufw'),
    path('git/', git, name='git'),
    path('screen/', screen, name='screen'),
    path('tar/', tar, name='tar'),
    path('k8s/', k8s, name='k8s'),
]
