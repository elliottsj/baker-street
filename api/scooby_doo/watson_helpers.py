from api.models import CanLIIDocument
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
    r = CanLIIDocument.search(title)
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
