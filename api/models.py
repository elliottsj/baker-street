from django.contrib.auth.models import User
from django.db import models
import pywatson.answer.evidence


class Page(models.Model):
    """A web page viewed in a ResearchSession."""
    url = models.TextField()
    title = models.TextField()
    content = models.TextField()

    user = models.ForeignKey(User)
    document = models.OneToOneField(Document)


class Document(models.Model):
    """A document in the corpus."""
    title = models.CharField(max_length=255)
    publish_date = models.DateField(null=True)

    def __str__(self):
        return self.title


class Evidence(models.Model):
    # pywatson.answer.evidence.Evidence attributes
    title = models.CharField(max_length=255)
    copyright = models.CharField(max_length=255)
    external_id = models.CharField(max_length=255)
    terms_of_use = models.CharField(max_length=255)
    document_path = models.CharField(max_length=255)
    text = models.TextField()
    confidence = models.FloatField()

    # pywatson.answer.evidence.MetadataMap attributes
    original_file = models.CharField(max_length=255)
    deepqa_id = models.CharField(max_length=255)
    corpus_name = models.CharField(max_length=255)
    docno = models.CharField(max_length=255)
    corpus_plus_docno = models.CharField(max_length=255)
    file_name = models.CharField(max_length=255)



class Question(models.Model):
    """A question submitted to Watson."""
    question_text = models.TextField()
    document = models.ForeignKey(Document, null=True)

    def __str__(self):
        return self.question_text
