from django.contrib.auth.models import User
from django.db import models


class Page(models.Model):
    """A web page viewed in a ResearchSession."""
    url = models.TextField()
    title = models.TextField()
    content = models.TextField()

    user = models.ForeignKey(User)
    document = models.OneToOneField(Document)


class Document(models.Model):
    """A document in the corpus."""
    title = models.CharField(max_length=200)
    publish_date = models.DateField(null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    """A question submitted to Watson."""
    question_text = models.TextField()
    document = models.ForeignKey(Document, null=True)

    def __str__(self):
        return self.question_text
