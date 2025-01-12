#!/bin/bash

# Sleep for 10 seconds to wait for rabbitmq to start
sleep 10

python -m celery -A Django_Celery_Flower beat -l debug --pidfile /var/run/celerbeat.pid --scheduler django_celery_beat.schedulers:DatabaseScheduler
