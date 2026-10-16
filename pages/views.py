import platform
import socket

import django
from django.conf import settings
from django.contrib.auth.models import User
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render

from .models import Task


def healthz(request):
    # One tiny query proves the database connection works.
    with connection.cursor() as cursor:
        cursor.execute('SELECT 1')
    return HttpResponse('ok', content_type='text/plain')


def home(request):
    with connection.cursor() as cursor:
        cursor.execute('SHOW server_version')
        db_version = cursor.fetchone()[0]
    context = {
        'app_env': settings.APP_ENV,
        'django_version': django.get_version(),
        'python_version': platform.python_version(),
        'db_version': db_version,
        'hostname': socket.gethostname(),
        'user_count': User.objects.count(),
        'open_tasks': Task.objects.filter(done=False).count(),
    }
    return render(request, 'pages/home.html', context)
