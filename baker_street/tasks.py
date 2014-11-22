from __future__ import absolute_import

from celery import shared_task, Celery
from baker_street.scooby_doo.watson_helpers import backgroundUpdate

@shared_task
def populate(session):
    backgroundUpdate(session)