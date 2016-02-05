from django.conf.urls import url

from .views import all_statuses


urlpatterns = [
    url(r'^all$', all_statuses),
]