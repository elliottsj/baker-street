from __future__ import absolute_import

from celery import shared_task

from baker_street.watson_helpers import backgroundUpdate


@shared_task
def populate(session):
    backgroundUpdate(session)