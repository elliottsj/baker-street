### Algo. For Context ###
from baker_street.models import VectorSet, CanLIIDocument
import nltk                 # for natural language and ML
from operator import itemgetter
from bs4 import BeautifulSoup # parsing HTML
import string
import requests
from django.db.models import F
import re

import logging, logging.config
import sys




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

def displayedContent(item):
    if item.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(item)):
        return False
    return True

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

    # remove bad text
    soup = BeautifulSoup(html)
    [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
    text = soup.body.getText()

    # classify text
    tokens = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(tokens)   # this takes awhile

    # collect terms that are the following
    types = ['NN', 'NNP', 'NNPS', 'NNS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP']
    wordZ = []
    [wordZ.append(i) for i in tagged if i[1] in types]

    # remove words with symbols and numbers
    words = []
    for i in wordZ:
        nope = 0
        for j in s:
            if j in i[0]:
                nope = 1
        if nope == 0:
            words.append(i)
    
    return words

def train(words, session):
    """ GOAL: Using clustering using EM cluster data to find context.
        This should be improving with add new data with iterations.

        FOR NOW: use weights, and change fix vector to work for our needs
    """

    words = [word[0] for word in words]
    words = list(set(words))
    queryset = VectorSet.objects.filter(word__in=words, session=session)
    queryset.weight = F('weight') + 1
    words = set(words) - set([l.word for l in queryset])
    new_vectors = [VectorSet(word=word, weight=1, session=session) for word in words]
    VectorSet.objects.bulk_create(new_vectors)

    return None

def updateContext(title, session):
    document = CanLIIDocument.search(title)
    if document == None:
        return
    train(relevent_words(document.content, False), session)

def getContext(session):
    querys = VectorSet.objects.filter(session=session)
    querys = querys.order_by('-weight')
    querys = querys[:29]
    s = ""
    for query in querys:
        s += " " + query.word
    return s[1:]

def assertion(text, context, n):
    sentences = re.split("\.", text)
    context = context.split()
    
    final = []
    count = 0
    for s in sentences:
        for c in context:
            if c in s:
                 final.append(s + '.')
                 count += 1
            if count >= n:
                return final

    if count < n:
        while count < n:
            final.append(sentences[count] + '.')
            count += 1

    return final

if __name__ == '__main__':
    print(relevent_words('http://en.wikipedia.org/wiki/Wikipedia', True))




