import datetime
from django.db import models


class Worker(models.Model):
    worker_name = models.CharField(max_length=200)

    def __str__(self):
        return self.worker_name


class Service(models.Model):
    worker_service = models.ForeignKey(Worker, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=200)
    duration = models.DurationField(default=datetime.timedelta(hours=1, minutes=0))
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.service_name


class Schedule(models.Model):
    worker_schedule = models.ForeignKey(Worker, on_delete=models.CASCADE)
