#!/bin/bash

# Sleep for 10 seconds to wait for rabbitmq to start
sleep 10

python -m celery -A Django_Celery_Flower worker -l debug -c 3 -Q critical,high,celery,mail,low,very_low
