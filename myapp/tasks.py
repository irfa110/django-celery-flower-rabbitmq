
from celery import shared_task

from django.contrib.auth.models import User


@shared_task
def simple_task_1(*args, **kwagrs):
    for i in range(100):
        print('Hello World')
    print('simple task')

@shared_task
def simple_task_2(*args, **kwargs):
    User.objects.create(username='Shama', password='Irfan@ali123')
    print('Simple task second')


@shared_task
def myname(*args, **kwargs):
    print(args, kwargs, "args and kwargs")
    for i in range(50):
        print('Irfan')
    print('Irfan Ali')



@shared_task
def print_periodic_message():
    print("This is a periodic task that prints a custom message.")
    print('*' * 100)