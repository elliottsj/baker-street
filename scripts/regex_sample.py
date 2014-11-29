from pycanlii.canlii import CanLII
from pycanlii.enums import LegislationType
import random as r

if __name__ == '__main__':
    canlii = CanLII("zxxdp6fyt5fatyfv44smrsbw")
    dbs = canlii.legislation_databases()

    l = []
    l2 = []
    for db in dbs:
        for piece in db:
            if piece.type == LegislationType.Regulation:
                l.append(piece)
            else:
                l2.append(piece)


    sample = r.sample(l, 600)

    l3 = []
    for item in sample:
        if len(item.title) > 220:
            continue
        s = ''
        s+= '"' + item.title + ', ' + item.citation + '",'
        s+= '"' + item.citation + '"'
        l3.append(s)

    sample = r.sample(l2, 400)
    for item in sample:
        if len(item.title) > 220:
            continue
        s = ''
        s+= '"' + item.title + ', ' + item.citation + '",'
        s+= '""'
        l3.append(s)

    r.shuffle(l3)
    s = ''
    for item in l3:
        s += item + '\n'

    f = open("data.csv", 'w')
    f.write(s)
    f.close()
