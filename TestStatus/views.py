from django.shortcuts import render
from django.views.decorators.http import require_safe

from .models import TestStatus


@require_safe
def all_statuses(request):
    statuses = [{
        'test_name': test_status.test.name,
        'short_description': test_status.status.short_description(),
        'comment': test_status.comment,
    } for test_status in TestStatus.objects.all()]
    context = {'statuses': statuses}
    return render(request, 'TestStatus/status_all.html', context)
