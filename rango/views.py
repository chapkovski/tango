from __future__ import absolute_import, unicode_literals
from django.shortcuts import render
from django_celery_beat.models import PeriodicTask, PeriodicTasks
# print(dir(django_celery_beat))
# Create your views here.
from django.http import HttpResponse
import random
from celery import app
from datetime import timedelta

from .tasks import *

def index(request):
    for p in PeriodicTask.objects.all():
        print(p)
    ppp10 = PeriodicTask.objects.get(name='add every 10')
    print('PPPPPPP~~!)!)!)!10', ppp10.enabled)
    ppp10.enabled = not ppp10.enabled
    print('PPPPPPP~~!)!)!)!10', ppp10.enabled)
    ppp10.save()
    PeriodicTasks.changed(ppp10)
    print('#####', len(PeriodicTask.objects.all()))

    # add.delay(4, 4)
    # filka.delay('asdf')
    # print('^^^^^^^^^^^^^', app.conf)
    # app.conf.update(
    #     CELERYBEAT_SCHEDULE={
    #         'perminute': {
    #             'task': 'tasks.add',
    #             'schedule': timedelta(seconds=3),
    #             'args': (1, 1)
    #         }
    #     }
    # )
    return HttpResponse("Rango says hey there partner!")
