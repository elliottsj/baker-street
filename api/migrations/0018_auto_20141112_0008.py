# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from pycanlii.canlii import CanLII

def populate_canlii(apps, scheme_editor):
    canlii = CanLII("zxxdp6fyt5fatyfv44smrsbw")
    case_dbs = canlii.case_databases()
    legis_dbs = canlii.legislation_databases()
    CanLIIDocument = apps.get_model("api", "CanLIIDocument")

    for db in case_dbs:
        for case in db:
            CanLIIDocument.objects.create(title=case.title, documentId=case.caseId, databaseId=case.databaseId,
                                          type=0, populated=False)


    for db in legis_dbs:
        for legis in db:
            CanLIIDocument.objects.create(title=legis.title, documentId=legis.legislationId,
                                          databaseId=legis.databaseId, type=1, populated=False)


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20141111_2359'),
    ]

    operations = [
        migrations.RunPython(populate_canlii)
    ]
