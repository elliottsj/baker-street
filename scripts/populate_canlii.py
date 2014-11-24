# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pickle
from zipfile import ZipFile

from django.db import migrations


def populate_canlii(apps, scheme_editor):
    CanLIIDocument = apps.get_model('baker_street', 'CanLIIDocument')

    with ZipFile('scripts/canlii_cases.pickle.zip', 'r') as z:
        with z.open('canlii_cases.pickle', 'r') as f:
            cases = pickle.load(f)

    case_list = [
        CanLIIDocument(title=case.title, documentId=case.caseId, databaseId=case.databaseId,
                       citation=case.citation, type=0, populated=False) for case in cases]

    # Insert documents in chunks
    for i in range(0, len(case_list), 750):
        CanLIIDocument.objects.bulk_create(case_list[i:i + 750])

    with ZipFile('scripts/canlii_legislations.pickle.zip', 'r') as z:
        with z.open('canlii_legislations.pickle', 'r') as f:
            legislations = pickle.load(f)

    legislations_list = [
        CanLIIDocument(title=legislation.title, documentId=legislation.legislationId,
                       databaseId=legislation.databaseId, citation=legislation.citation, type=1,
                       populated=False) for legislation in legislations]
    CanLIIDocument.objects.bulk_create(legislations_list)


class Migration(migrations.Migration):

    dependencies = [
        ('baker_street', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_canlii),
    ]
