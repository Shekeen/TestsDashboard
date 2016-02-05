from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class TestStatus(models.Model):
    class Meta:
        verbose_name_plural = 'Test statuses'

    test = models.ForeignKey('Tests.Test')
    status = models.ForeignKey('Tests.Status')
    last_status_update = models.DateTimeField(default=timezone.now)
    comment = models.TextField(null=True)
    last_comment_update = models.DateTimeField(default=timezone.now)

    def update_status(self, status):
        self.status = status
        self.last_status_update = timezone.now()
        self.save()

    def update_comment(self, comment):
        self.comment = comment
        self.last_comment_update = timezone.now()
        self.save()

    def __str__(self):
        return '<TestStatus: {}, status: {}>'.format(self.test.name, self.status.short_description())
