from app import init_celery

app = init_celery()
app.conf.imports = app.conf.imports + ("app.utils.task.task_scheduler",)