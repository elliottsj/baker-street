import gzip
import json
import pickle
from pycanlii import CanLII, Case


def get_canlii_documents():
    """
    Download every CanLii document and return the lists of cases and legislation

    :return: tuple of (list of cases, list of legislation)
    """
    cases = []
    legislations = []

    canlii = CanLII('zxxdp6fyt5fatyfv44smrsbw')
    case_dbs = canlii.case_databases()
    legislation_dbs = canlii.legislation_databases()

    # count = 0
    for db in case_dbs:
        for case in db:
            cases.append(case)
            # count += 1
            # if count >= 10000:
            #     break
    # for db in legislation_dbs:
    #     for legislation in db:
    #         legislations.append(legislation)

    return cases, legislations


class CaseEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Case):
            return {
                'model': 'baker_street.canliidocument',
                'fields': {
                    'title': o.title,
                    'databaseId': o.databaseId,
                    'documentId': o.caseId,
                    'type': 0,
                    'citation': o.citation,
                    'populated': False
                }
            }
        return super().default(o)


if __name__ == '__main__':
    cases, legislations = get_canlii_documents()

    with gzip.open('canlii_cases.json.gz', 'wt') as f:
        json.dump(cases, f, cls=CaseEncoder)
    # with open('canlii_legislations.json', 'wb') as f:
    #     json.dump(legislations, f, pickle.HIGHEST_PROTOCOL)
