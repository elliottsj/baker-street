from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=200)
    publish_date = models.DateField(null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    question_text = models.TextField()
    document = models.ForeignKey(Document, null=True)

    def __str__(self):
        return self.question_text
