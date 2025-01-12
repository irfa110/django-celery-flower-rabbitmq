import logging
# import os

from celery.result import AsyncResult


logger = logging.getLogger(__name__)


def create_celery_task(task_fn, payload, eta):
    try:
        task_id = None
        logger.debug(f"Creating celery task for fn: {task_fn}"
                     f" with payload {payload} and eta {eta}")
        res = task_fn.apply_async(kwargs=payload, eta=eta)
        logger.debug(f"Created task with id {res.id}")
        task_id = res.id
        return task_id
    except Exception as ex:
        logger.error(f"error while creating task {task_fn}"
                     f" error: {ex}"
                     f" with payload {payload} and eta {eta}")
        return None


def delete_task(task_id, queue_name):
    # if os.getenv('GOOGLE_CLOUD_PROJECT'):
    #     delete_gcloud_app_engine_task(queue_name, task_id)
    # else:
    task_result = AsyncResult(task_id)
    logger.info(f"Task with id {task_id} has status "
                f"{task_result.status}"
                f" queue_name {queue_name}")
    if task_result.status in ['SENT', 'RECEIVED', 'PENDING']:
        task_result.revoke()
