import logging
import collections
from baker_street.exceptions import InvalidDocumentException
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django_enumfield import enum
from baker_street.enums import Website
from pycanlii.canlii import CanLII
from pycanlii.case import Case
from pycanlii.legislation import Legislation
from django.core.exceptions import MultipleObjectsReturned
import re
import random

class Website(models.Model):
    url = models.CharField(max_length=255, default="")

class Sitelist(models.Model):
    websites = models.ManyToManyField(Website)

    def add_site(self, sites):
        if isinstance(sites, str):
            w = Website.objects.get_or_create(url=sites)
            self.websites.add(w[0])
            self.save()
            return w[0]
        elif isinstance(sites, collections.Iterable):
            for site in sites:
                w = Website.objects.get_or_create(url=site)
                self.websites.add(w[0])
            self.save()

class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                              **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(verbose_name='first name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=30, blank=True)
    email = models.EmailField(verbose_name='email address', unique=True)
    is_staff = models.BooleanField(verbose_name='staff status', default=False,
        help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField(verbose_name='active', default=True,
        help_text='Designates whether this user should be treated as '
                  'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField(verbose_name='date joined', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def setCurrentSession(self, new_id):
        old = ResearchSession.objects.filter(user=self, current=True)
        if (len(old) == 1):
            old[0].current = False
            old[0].save()
        new = ResearchSession.objects.filter(id=new_id)
        new = new[0]
        new.current = True
        new.save()
        return new

    @property
    def current_session(self):
        return ResearchSession.objects.filter(user=self, current=True)[0]

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Returns the short name for the user."""
        return self.first_name

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True


class ResearchSession(models.Model):
    """A sequence of pinned Pages and prioritized Contexts"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=255)
    current = models.BooleanField(default=False)

    sitelist = models.OneToOneField(Sitelist)

    def setCurrentPage(self, new):
        old = Page.objects.filter(research_session=self, most_recent=True)
        if (len(old) == 1):
            old[0].most_recent = False
            old[0].save()
        new.most_recent = True
        new.save()
        return new

    @property
    def current_page(self):
        return Page.objects.get(research_session=self, most_recent=True)

class CanLIIDocument(models.Model):
    title = models.TextField()
    documentId = models.CharField(max_length=64)
    databaseId = models.CharField(max_length=64)
    type = models.IntegerField(db_index=True) # 0 is case, 1 is statutes, 2 is regulation
    populated = models.BooleanField(default=False)
    url = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    repealed = models.NullBooleanField(default=None)
    citation = models.CharField(max_length=255, db_index=True)

    canlii = CanLII("zxxdp6fyt5fatyfv44smrsbw")

    @staticmethod
    def search(title):
        # Search for a case citation
        regex = re.compile("([0-9]{4} [a-zA-Z0-9]+ [0-9]+ \([a-zA-Z0-9- ]+\))")
        search = regex.search(title)
        if search != None: # it's a case
            # It's a valid case
            snippet = title[search.regs[0][0]:search.regs[0][1]]
            snippet = snippet.upper()
            snippet = snippet.replace("CANLII", "CanLII")
            try:
                model = CanLIIDocument.objects.filter(citation=snippet)
                if len(model) == 0:
                    return None
                else:
                    model = model[0]
            except MultipleObjectsReturned:
                logging.warning("Apparently cases can potentially return more than 1 result, handle this")
                return None

            if not model.populated:
                input = { 'caseId' : { 'en' : model.documentId },
                          'databaseId' : model.databaseId,
                          'title' : model.title,
                          'citation' : model.citation
                          }
                case = Case(input, "zxxdp6fyt5fatyfv44smrsbw")
                model.content = case.content
                model.url = case.url
                model.populated = True
                model.type = 0
                model.save()
            return model

        regex = re.compile("[A-Z]+( [0-9]{4}(-[0-9]{2})?)?(,)? c (([A-Z]*[0-9]*)|([A-Z]+\.[0-9]+)|([A-Z]+-[0-9]+\.[0-9]+))")
        search = regex.search(title)
        if search != None: # it's a Statute
            snippet = title[search.regs[0][0]:search.regs[0][1]]
            models = CanLIIDocument.objects.filter(citation=snippet).exclude(repealed=True)
            # There's a bug here when it's just None and hasen't been loaded yet it could get psoted
            # even if it's repealed. Should do a loop checking for repealing legislation if length
            # of models is longer than 1
            if len(models) == 0:
                return None
            model = models[0]
            if not model.populated:
                input = { 'legislationId' :  model.documentId,
                          'databaseId' : model.databaseId,
                          'title' : model.title,
                          'citation' : model.citation,
                          'type' : "STATUTE"
                }
                legis = Legislation(input, "zxxdp6fyt5fatyfv44smrsbw")
                model.content = legis.content
                model.url = legis.url
                model.repealed = legis.repealed
                model.populated = True
                model.type = 1
                model.save()
            return model

        #This regex ~88% of the time, AKA good enough for now
        regex = re.compile("\w(?=((?:[Q][^.](?=( ?))\2)*))\1(?=((?:\w(?=( ?))\4(?=((?:[1](?=( ?))\6)*))\5)?))\3(?=([\-]*))\7(?=((?:(?=(\w*))\9(?=( ?))\10[^D]\w(?=(1*))\11(?=([Q]*))\12)?))\8(?=((?:\w(?=((?:(?=((?:(?=( ?))\16(?=(\)?))\17(?=((?:[1][^D])*))\18)*))\15\w)*))\14)*))\13[^J]\d(?=((?:(?=((?:(?=(\w*))\21(?=((?:[^D](?=(\d?))\23[^D])?))\22)*))\20(?=([^ ]?))\24[^D])?))\19[^D](?=(\w*))\25(?=([^D]*))\26")
        search = regex.search(title)
        if search != None: # it's a regulation
            snippet = title[search.regs[0][0]:search.regs[0][1]]
            models = CanLIIDocument.objects.filter(citation=snippet).exclude(repealed=True)
            # There's a bug here when it's just None and hasen't been loaded yet it could get psoted
            # even if it's repealed. Should do a loop checking for repealing legislation if length
            # of models is longer than 1
            if len(models) == 0:
                return None
            model = models[0]
            if not model.populated:
                input = { 'legislationId' :  model.documentId,
                          'databaseId' : model.databaseId,
                          'title' : model.title,
                          'citation' : model.citation,
                          'type' : "REGULATION"
                }
                legis = Legislation(input, "zxxdp6fyt5fatyfv44smrsbw")
                model.content = legis.content
                model.url = legis.url
                model.repealed = legis.repealed
                model.populated = True
                model.type = 2
                model.save()
            return model




        # STILL NEED TO LOOK FOR REGULATIONS



        # If there is no match on the citation we're assuming it's not a document in CanLII
        # This is a somewhat naive assumption however it will be true in the vast majority of cases
        if search == None:
            return None


class Page(models.Model):
    """A web page viewed in a ResearchSession."""
    page_url = models.TextField()
    title = models.TextField(blank=True)
    content = models.TextField(blank=True)
    most_recent = models.BooleanField(default=False)
    snippet = models.BooleanField(default=False)

    research_session = models.ForeignKey(ResearchSession)

class Document(models.Model):
    """A document in the corpus."""
    title = models.CharField(max_length=255)
    publish_date = models.DateField(null=True)
    url = models.CharField(max_length=255)
    pinned = models.BooleanField(default=False)
    content = models.TextField()
    type = models.IntegerField()
    source = models.CharField(max_length=255, default="CanLII")

    session = models.ForeignKey(ResearchSession)
    page = models.ForeignKey(Page)
    canlii = models.ForeignKey(CanLIIDocument)

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


class Context(models.Model):
    """Key words/strings used to prioritize documents in ResearchSessions."""
    value = models.TextField()

    research_session = models.ForeignKey(ResearchSession)


class Question(models.Model):
    """A question submitted to Watson."""
    question_text = models.TextField()
    document = models.ForeignKey(Document, null=True)

    def __str__(self):
        return self.question_text


class VectorSet(models.Model):
    word = models.CharField(max_length=255, db_index=True)
    weight = models.IntegerField()

    session = models.ForeignKey(ResearchSession)

def _get_new():
        s = ''
        for i in range(16):
            s += random.choice("qwertyuiopasdfghjklzxcvbnm")
        if InviteCode.objects.filter(code=s).exists():
            return InviteCode._get_new()
        return s

class InviteCode(models.Model):
    code = models.CharField(max_length=16, default=_get_new)
    used = models.BooleanField(default=False)

