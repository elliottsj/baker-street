from pywatson.watson import Watson
from pywatson.question.watson_question import WatsonQuestion
from pycanlii.canlii import CanLII
from bs4 import BeautifulSoup
import requests

def f(text):
    watson = Watson(url='https://watson-wdc01.ihost.com/instance/507/deepqa/v1',
                    username='ut_student5', password='9JwXacPH')

    question = WatsonQuestion(text, formatted_answer=True, items=3,
                          evidence_request= { "items": 2, "profile" : "yes"})

    answer = watson.ask_question(text, question=question)
    return answer

def g(title):
    canlii = CanLII("zxxdp6fyt5fatyfv44smrsbw")
    r = canlii.search(title, 1, 0)
    if len(r) != 1:
        return
    r = r[0]
    b = BeautifulSoup(r.content)
    text = b.get_text()
    return text

def h(t):
    t = g(t)
    s = t.split('\n')
    mid = (len(s) * 3) // 4
    answer = f(s[mid])
    return answer.evidence_list

def get_documents(t):
    evidence = h(t)
    canlii = CanLII("zxxdp6fyt5fatyfv44smrsbw")
    l = []
    for e in evidence:
        try:
            x = canlii.search(e.title, 1, 0)
            if len(x) == 1:
                l.append(x[0])
        except requests.exceptions.HTTPError:
            pass



    return l

if __name__ == '__main__':
    #evidence = h("G. (Re), 2010 CanLII 5993 (ON CCB)")
    objs = get_documents("G. (Re), 2010 CanLII 5993 (ON CCB)")
    x = [x.title for x in objs]
    print(x)


### Make this a migration somehow
def populate():
    canlii = CanLII("zxxdp6fyt5fatyfv44smrsbw")
    case_dbs = canlii.case_databases()
    legis_dbs = canlii.legislation_databases()

    for db in case_dbs:
        for case in db:
            api.models.CanLIIDocument.objects.create(title=case.title, documentId=case.caseId,
                                                     databaseId=case.databaseId, populated=False)

    for db in legis_dbs:
        for legis in db:
            api.models.CanLIIDocument.objects.create(title=legis.title, documentId=legis.legislationId,
                                                     databaseId=legis.databaseId, populated=False)


def search(title):
    models = CanLIIDocument.objects.filter(title=title)

    ## Attempt to coax out some documents
    if (len(models) == 0):
        words = title.split()
        while(len(models) == 0 and len(words) > 0):
            words.pop()
            s = words[0]
            for i in range(1, len(words)):
                s+= ' ' + words[i]
            models = CanLIIDocument.objects.filter(title=title)

    # Say fuck it
    if (len(models) == 0):
        return None

    # Deal with too many results, probably by crying, hopefully with a fancy algorithm
    # I'm envisioning something that compares based on words starting from the begining
    if (len(models) > 1):
        pass

    model = models[0]
    # this will require knowing if it's legislation or a case, should deal with this
    if not model.populated:
        pass #remember to save when this is done

    return model


