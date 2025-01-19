# myproject/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from kombu import Queue, Exchange

# Set default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Celery_Flower.settings')

# Create a Celery application instance
app = Celery('Django_Celery_Flower')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


# Schedule periodic tasks using beat_schedule
app.conf.beat_schedule = {
    # Run every minute
    'run-every-minute': {
        'task': 'myapp.tasks.print_periodic_message',
        'schedule': crontab(minute='*'),
        'args': (),
    },

    # Run every day at midnight
    'run-every-day': {
        'task': 'myapp.tasks.print_periodic_message',
        'schedule': crontab(minute=0, hour=0),
        'args': (),
    },

    # Run every week at midnight on Sunday
    'run-every-week': {
        'task': 'myapp.tasks.print_periodic_message',
        'schedule': crontab(minute=0, hour=0, day_of_week='sunday'),
        'args': (),
    },

    # Run every month after 5 months (starting from the 1st day of the 6th month)
    'run-every-month-after-5-months': {
        'task': 'myapp.tasks.print_periodic_message',
        'schedule': crontab(minute=0, hour=0, day_of_month=1, month_of_year='6-12'),
        'args': (),
    },
}


app.conf.task_default_queue = 'celery'

app.conf.task_queues = (
    Queue('critical',
          Exchange('critical'),
          routing_key='critical',
          consumer_arguments={'x-priority': 11}),
    Queue('high',
          Exchange('high'),
          routing_key='high',
          consumer_arguments={'x-priority': 10}),
    Queue('mail',
          Exchange('mail'),
          routing_key='mail',
          consumer_arguments={'x-priority': 9}),
    Queue('celery',
          Exchange('celery'),
          routing_key='celery',
          consumer_arguments={'x-priority': 8}),
    Queue('low',
          Exchange('low'),
          routing_key='low',
          consumer_arguments={'x-priority': 7}),
    Queue('very_low',
          Exchange('very_low'),
          routing_key='very_low',
          consumer_arguments={'x-priority': 6},
          queue_arguments={'x-queue-mode': 'lazy'}),
)


app.conf.task_routes = {
    'utils.tasks.*': {
        'queue': 'low',
        'routing_key': 'low',
    },
    # 'services.tasks.chat.*': {
    #     'queue': 'high',
    #     'routing_key': 'high',
    # },
    # 'services.tasks.call.*': {
    #     'queue': 'critical',
    #     'routing_key': 'critical',
    # }
}


task_default_exchange = 'high'
task_default_exchange_type = 'direct'
task_default_routing_key = 'high'
