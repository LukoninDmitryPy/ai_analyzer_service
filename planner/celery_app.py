from celery import Celery
import os
from dotenv import load_dotenv

from utils.log_utils import getLogger


load_dotenv()

celery = Celery(
    'celery_app',
    broker=f'amqp://{os.getenv("RBMQ_USER")}:{os.getenv("RBMQ_PASS")}@{os.getenv("RBMQ_HOST")}:{os.getenv("RBMQ_PORT")}/',
    include=['planner.tasks']
)

logger = getLogger(__name__)

celery.conf.beat_schedule = {
    'check_route': {
        'task': 'planner.tasks.check_route',
        'schedule': os.getenv('SCHEDULE'),
    },
}
celery.conf.timezone = 'UTC'
