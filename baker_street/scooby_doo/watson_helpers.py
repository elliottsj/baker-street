from baker_street.context_helpers import getContext, assertion
from baker_street.models import CanLIIDocument
from pywatson.watson import Watson
from pywatson.question.watson_question import WatsonQuestion
from pycanlii.canlii import CanLII
from bs4 import BeautifulSoup
from baker_street.exceptions import InvalidDocumentException
import requests


watson = Watson(url='https://watson-wdc01.ihost.com/instance/507/deepqa/v1',
                    username='ut_student5', password='9JwXacPH')

def call_watson(body, session, items=3, calls=1):
    context = getContext(session)
    text = assertion(body, False, context, calls)[0]

    question = WatsonQuestion(text, formatted_answer=True, items=items, context=context,
                          evidence_request= { "items": 2, "profile" : "yes"})

    answer = watson.ask_question(text, question=question)
    return answer

def search_db(title):
    r = CanLIIDocument.search(title)
    return r.content

def generate_questions_and_call_watson(t, session, items, calls):
    body = search_db(t)

    answer = call_watson(body, session, items, calls)
    return answer.evidence_list

def get_documents(t, session, items=3, calls=1):
    evidence = generate_questions_and_call_watson(t, session, items, calls)
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

def backgroundUpdate(session):
    calls = 10 # Constant number of calls
    items = 3 # Constant number of items

    page = session.current_page
    canliipage = CanLIIDocument.search(page.title)
    content = canliipage.content
    context = getContext(session)

    questions = assertion(content, False, context, calls)

    for text in questions:
        question = WatsonQuestion(text, formatted_answer=True, items=items, context=context,
                                    evidence_request= { "items": 2, "profile" : "yes"})
        answer = watson.ask_question(text, question=question)
        evidence = answer.evidence_list
        for e in evidence:
            try:
                document = CanLIIDocument.search(e.title)
                if document != None:
                    session.document_set.create(title=document.title, url=document.url, pinned=False, content=e.text,
                                                type=document.type, page=page)
            except requests.exceptions.HTTPError:
                pass





if __name__ == '__main__':
    objs = get_documents("G. (Re), 2010 CanLII 5993 (ON CCB)")
    x = [x.title for x in objs]
    print(x)

