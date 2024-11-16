import requests

from planner.celery_app import celery, logger


@celery.task(default_retry_delay=30)
def check_route():
    """Task to check the route and upload a file."""
    try:
        with open('some_prod.xml', 'rb') as file:
            response = requests.get(
                "http://127.0.0.1:8000/check_route/"
            )
        if response.status_code == 200:
            logger.info("Route is working correctly")
        else:
            logger.error("Route is not working correctly, status: %d", response.status_code)
    except requests.exceptions.RequestException as e:
        logger.exception(f"Request error: {e}")
    except FileNotFoundError as e:
        logger.exception(f"File not found: {e}")

@celery.task
def simple_task():
    return "Task executed successfully"
