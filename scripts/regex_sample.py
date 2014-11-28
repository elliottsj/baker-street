from pycanlii.canlii import CanLII
from pycanlii.enums import LegislationType
import random as r

if __name__ == '__main__':
    canlii = CanLII("zxxdp6fyt5fatyfv44smrsbw")
    dbs = canlii.legislation_databases()

    l = []
    for db in dbs:
        for piece in db:
            if piece.type == LegislationType.Regulation:
                l.append(piece)


    sample = r.sample(l, 600)
    s = ''
    for item in sample:
        if len(item.title) > 220:
            continue
        s+= '"' + item.title + ', ' + item.citation + '",'
        s+= '"' + item.citation + '"\n'

    f = open("data.csv", 'w')
    f.write(s)
    f.close()
