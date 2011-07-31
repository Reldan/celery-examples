from time import sleep
from celery.decorators import task


@task
def processing_video_task(file_name):
    print "processing video %s" % file_name
    sleep(2)
    return "ok"

@task
def loading_video_task(file_name):
    print "loading video %s" % file_name
    sleep(1)
    return "ok"