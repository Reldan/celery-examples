import sys

sys.path.append('.')

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "myuser"
BROKER_PASSWORD = "mypassword"
BROKER_VHOST = "myvhost"

CELERY_RESULT_BACKEND = "amqp"

CELERY_IMPORTS = ("tasks", )
CELERY_ROUTES = {"tasks.processing_video_task": {"queue": "processing"},
                 "tasks.loading_video_task": {"queue": "loading"}}