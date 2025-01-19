import logging
from datetime import datetime, timezone, timedelta
from django.shortcuts import render
from .tasks import simple_task_1, simple_task_2, myname
from utils.tasks_helpers import create_celery_task

def index(request):
    return render(request, 'index.html')


logger = logging.getLogger(__name__)


def view1(request):
    logger.info('Starting view1()')
    if request.method == 'POST':
        # simple_task_1.delay()
        payload = {
            'x': 1,
        }
        eta = datetime.utcnow().replace(
            tzinfo=timezone.utc) + timedelta(seconds=60)
        create_celery_task(
            myname,
            payload,
            eta
        )
        logger.info('Finished view1()')
        return render(request, 'index.html', context={'button1': True})


def view2(request):
    if request.method == 'POST':
        simple_task_2.delay()
        logger.info('Finished view2()')
        return render(request, 'index.html', context={'button2': True})
