### Algo. For Context ###
import nltk                 # for natural language and ML
from operator import itemgetter
from bs4 import BeautifulSoup # parsing HTML
import string
import requests
from api.models import VectorSet, CanLIIDocument
from django.db.models import F

# string of symbols and nums
s = []
for c in range(len(string.punctuation) - 1):
    s.append(string.punctuation[c])
for d in range(len(string.digits) - 1):
    s.append(string.digits[d])

# cluster for session
# cluster = nltk.cluster.api.ClusterI()
# vector of classified words
vector = {}


def relevent_words(url, is_url):
    '''
    Badly pasrses html text and classifies text based on parts of speech.
    Then selects desired types of words and return in list with its part
    of speach.

    (str)   url - either the url or html text
    (bool)  us_url - True of url is a url, false if html text
    '''
    # get text
    if is_url:
        html = requests.get(url).text
    else:
        html = url

    soup = BeautifulSoup(html)
    text = soup.getText()

    # classify text
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)   # this takes awhile

    # collect terms that are the following
    types = ['NN', 'NNP', 'NNPS', 'NNS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP']
    words = []
    [words.append(i) for i in tagged if i[1] in types]

    # remove some unwanted words
    # fix this later :P
    bad_words= ['css', 'DOCTYPE', 'html', 'nbsp', 'rdquo', 'Code/footer', 'bsp',
                'htmlsync', 'Times', 'New', 'Roman', 'margin', 'link', 'jQuery',
                'setReflexRecordNoteupCountText', 'line', 'ol','ul', 'var', 'lang',
                'class', 'linkCount', 'title', 'closeButton', 'closeButtonSkin',
                'documentMeta', 'click', 'function', 'toSelect', 'tf', 'selectText',
                'toSelect', 'toSelect', 'callReflexRecordNoteupCount',
                'toggleContent', 'decisionHeadnotes', 'noteupCountUrl', 'document',
                'getTipTitleString', 'documents', 'Home', 'rsaquo', 'ldquo', 'lt',
                'gt', 'https', 'http', 'g', 's', 'End', 'Piwik','followScroll',
                'notHighlighted', 'Act', 'as', 'As', 'In', 'in', 'CanLII', 'be',
                'had', 'process', 'hearing', 'plaintiff', 'case', 'are', 'did',
                'rsquo', 'Data', 'do', 'No', 'ESRTW', 'been', 'page', 'was',
                'reflex', 'were', 'have']
    new_words = []
    [new_words.append(i) for i in words if i[0] not in bad_words]

    # remove words with symbols and numbers
    words = []
    for i in new_words:
        nope = 0
        for j in s:
            if j in i[0]:
                nope = 1
        if nope == 0:
            words.append(i)
    
    return words

def train(words, session):
    ''' GOAL: Using clustering using EM cluster data to find context.
        This should be improving with add new data with iterations.

        FOR NOW: use weights, and change fix vector to work for our needs
    '''
    # add words to vector

    for i in words:
        result, created = VectorSet.objects.get_or_create(word=i[0], session=session, defaults={'weight' : 1})
        if not created:
            result.weight = F('weight') + 1
            result.save()

def updateContext(title, session):
    document = CanLIIDocument.search(title)
    train(relevent_words(document.content, False), session)

def getContext(session):
    querys = VectorSet.objects.filter(session=session)
    querys = querys.order_by('-weight')
    querys = querys[:29]
    s = ""
    for query in querys:
        s += " " + query.word
    return s[1:]


    
