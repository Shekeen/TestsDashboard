from __future__ import unicode_literals

from django.db import models


class Status(models.Model):
    class Meta:
        verbose_name_plural = 'Statuses'

    description = models.CharField(max_length=1400)
    failure_code = models.IntegerField()

    def is_success(self):
        return self.failure_code == 0

    def short_description(self, max_length=30):
        if len(self.description) <= max_length:
            return self.description
        else:
            return self.description[:max_length-3] + '...'

    def __str__(self):
        return '<Status: {}>'.format(self.short_description())


class Test(models.Model):
    class Meta:
        unique_together = ('name',)

    name = models.CharField(max_length=1400)
    description = models.TextField(blank=True)

    def __str__(self):
        return '<Test: {}>'.format(self.name)
