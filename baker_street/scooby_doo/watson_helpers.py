from baker_street.models import CanLIIDocument
from pywatson.watson import Watson
from pywatson.question.watson_question import WatsonQuestion
from pycanlii.canlii import CanLII
from bs4 import BeautifulSoup
from baker_street.exceptions import InvalidDocumentException
import requests

def call_watson(text):
    watson = Watson(url='https://watson-wdc01.ihost.com/instance/507/deepqa/v1',
                    username='ut_student5', password='9JwXacPH')

    question = WatsonQuestion(text, formatted_answer=True, items=3,
                          evidence_request= { "items": 2, "profile" : "yes"})

    answer = watson.ask_question(text, question=question)
    return answer

def search_db(title):
    r = CanLIIDocument.search(title)
    b = BeautifulSoup(r.content)
    text = b.get_text()
    return text

def generate_questions_and_call_watson(t):
    t = search_db(t)
    s = t.split('\n')
    mid = (len(s) * 3) // 4
    answer = call_watson(s[mid])
    return answer.evidence_list

def get_documents(t, session):
    evidence = generate_questions_and_call_watson(t)
    canlii = CanLII("zxxdp6fyt5fatyfv44smrsbw")
    l = []
    for e in evidence:
        try:
            d = CanLIIDocument.search(e.title)
            if d != None:
                document = session.document_set.create(title=d.title, url=d.url, pinned=False,
                                                  content=e.text, type=d.type)
                l.append(document)
        except InvalidDocumentException:
            pass
        except requests.exceptions.HTTPError:
            pass

    return l

if __name__ == '__main__':
    objs = get_documents("G. (Re), 2010 CanLII 5993 (ON CCB)")
    x = [x.title for x in objs]
    print(x)

