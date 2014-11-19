### Algo. For Context ###
import nltk                 # for natural language and ML
from operator import itemgetter
from bs4 import BeautifulSoup # parsing HTML
import string
import requests

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
# phase number
phase = 0


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

def train(words, phase):
    ''' GOAL: Using clustering using EM cluster data to find context.
        This should be improving with add new data with iterations.

        FOR NOW: use weights, and change fix vector to work for our needs
    '''
    # add words to vector
    for i in words:
        if i[0] not in vector:
            vector[i[0]] = 1
        else:
            vector[i[0]] = vector[i[0]] + 1

    # fix vector every 5 iterations
    if phase == 4:
        for item in vector.keys():
            if vector[item] < 5:
                vector.pop(item)
        phase = 0
    
    return phase + 1

def get_context(num):
    '''
    Return contect for
    (int) num is the number of items wanted back
    '''
    v_list = list(vector.items())
    final = sorted(v_list, key=itemgetter(1), reverse=True)
    
    return final[0:num-1]

if __name__ == '__main__':
    # some testing
    w = relevent_words("https://www.canlii.org/en/on/onlrb/doc/2001/2001canlii6145/2001canlii6145.html?searchUrlHash=AAAAAQAWZW1wbG95bWVudCB0ZXJtaW5hdGlvbgAAAAAB", True)
    phase = train(w, phase)
    w = relevent_words("https://www.canlii.org/en/on/onlrb/doc/2005/2005canlii11562/2005canlii11562.html?searchUrlHash=AAAAAQAWZW1wbG95bWVudCB0ZXJtaW5hdGlvbgAAAAAB", True)
    phase = train(w, phase)
    w = relevent_words("https://www.canlii.org/en/on/onwsiat/doc/2010/2010onwsiat637/2010onwsiat637.html?searchUrlHash=AAAAAQAWZW1wbG95bWVudCB0ZXJtaW5hdGlvbgAAAAAB",True) 
    phase = train(w, phase)
    w = relevent_words("https://www.canlii.org/en/on/onsc/doc/2012/2012onsc6387/2012onsc6387.html?searchUrlHash=AAAAAQAWZW1wbG95bWVudCB0ZXJtaW5hdGlvbgAAAAAB", True)
    phase = train(w, phase)
    w = relevent_words("https://www.canlii.org/en/on/onlrb/doc/2004/2004canlii14309/2004canlii14309.html?searchUrlHash=AAAAAQAWZW1wbG95bWVudCB0ZXJtaW5hdGlvbgAAAAAB", True)
    phase = train(w, phase)
    
