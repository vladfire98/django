from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import os


# Create your views here.
menu = ["Этот", "список", "вызывается", "в", "файле" ,"/homepage/views.py"]

DEFAULT_TITLE = "Главная страница"
TITLE = os.getenv("PAGE_TITLE", DEFAULT_TITLE)

def index(request):
    #return HttpResponse("<h1>This is HomePage!</h1>")
    return render(request, 'homepage/index.html', {'menu': menu, 'title': TITLE})

def qwerty(request):
    return HttpResponse("<h1>QWERTY!</h1>")

def qwe(request):
    #return HttpResponse("<h1>This is HomePage!</h1>")
    return render(request, 'homepage/qwe.html')

def docker(request):
    return render(request, 'homepage/docker.html', {'title': 'Docker'})

def systemd(request):
    return render(request, 'homepage/systemd.html', {'title': 'Systemd'})

def samba(request):
    return render(request, 'homepage/samba.html', {'title': 'Samba'})

def disk(request):
    return render(request, 'homepage/disk.html', {'title': 'LVM'})

def swap_linux(request):
    return render(request, 'homepage/swap_linux.html', {'title': 'Swap Linux'})

def firewalld(request):
    return render(request, 'homepage/firewalld.html', {'title': 'firewalld'})

def cisco(request):
    return render(request, 'homepage/cisco.html', {'title': 'Cisco'})


def postgresql(request):
    return render(request, 'homepage/postgresql.html', {'title': 'PostgreSQL'})


def netsh(request):
    return render(request, 'homepage/netsh.html', {'title': 'Netsh'})

def haproxy(request):
    return render(request, 'homepage/haproxy.html', {'title': 'HAProxy'})

def ufw(request):
    return render(request, 'homepage/ufw.html', {'title': 'Ufw'})

def git(request):
    return render(request, 'homepage/git.html', {'title': 'Git'})

def screen(request):
    return render(request, 'homepage/screen.html', {'title': 'screen'})

def tar(request):
    return render(request, 'homepage/tar.html', {'title': 'tar'})

def k8s(request):
    return render(request, 'homepage/k8s.html', {'title': 'k8s'})

def ovswitch(request):
    return render(request, 'homepage/ovs.html', {'title': 'ovswitch'})

def release_handler(request):
    return render(request, 'homepage/release_handler.html', {'title': 'Release Handler'})

def ip_linux(request):
    return render(request, 'homepage/ip_linux.html', {'title': 'IP Linux'})

def isolating_nic(request):
    return render(request, 'homepage/isolating_nic.html', {'title': 'Isolating nic'})

def veth(request):
    return render(request, 'homepage/veth.html', {'title': 'Veth'})

def PackageNotFoundError(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
