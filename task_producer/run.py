import tasks


def make_tasks():
    pending_tasks = []

    print "Dispatching tasks"
    for x in xrange(1000):
        pending_tasks.append(tasks.loading_video_task.delay(x))
        pending_tasks.append(tasks.processing_video_task.delay(x))

    results = get_task_results(pending_tasks)
    
    print "Results: %s" % results
    
def get_task_results(tasks):
    """
    Wait for all tasks to complete and return a list containing the result of
    each task.
    """
    results = []

    for task in tasks:
        task.wait()
        if not task.successful():
            raise Exception(task.result)
        results.append(task.result)

    return results


if __name__ == '__main__':
    print "Provision tasks:"
    make_tasks()
