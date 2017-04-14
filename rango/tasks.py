from __future__ import absolute_import, unicode_literals
from celery import Celery
app = Celery( broker='redis://localhost:6379/0')


@app.task
def add(x, y):
    return x + y
