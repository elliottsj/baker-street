import pickle
from pycanlii import CanLII


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

    for db in case_dbs:
        for case in db:
            cases.append(case)
    for db in legislation_dbs:
        for legislation in db:
            legislations.append(legislation)

    return cases, legislations

if __name__ == '__main__':
    cases, legislations = get_canlii_documents()

    with open('canlii_cases.pickle', 'wb') as f:
        pickle.dump(cases, f, pickle.HIGHEST_PROTOCOL)
    with open('canlii_legislations.pickle', 'wb') as f:
        pickle.dump(legislations, f, pickle.HIGHEST_PROTOCOL)
