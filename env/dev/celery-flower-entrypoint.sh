#!/bin/bash

# Sleep for 10 seconds to wait for rabbitmq to start
sleep 10

python -m celery -A Django_Celery_Flower flower --basic_auth=admin:init1234