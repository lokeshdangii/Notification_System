from celery import Celery

# Create a Celery app instance with Redis as the broker
celery = Celery(
    "notification_tasks",
    broker="redis://localhost:6379/0",  # Redis default
    backend="redis://localhost:6379/0"
)
