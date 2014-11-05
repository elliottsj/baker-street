class CanLIIDocument:

    def __init__(self, canlii_object):
        self.title = canlii_object.title
        self.url = canlii_object.url

    def json(self):
        return { "title" : self.title, "url" : self.url}

