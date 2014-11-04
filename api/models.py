from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


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


class ResearchSession(models.Model):
    """A sequence of pinned Pages and prioritized Contexts"""
    name = models.CharField(max_length=255)

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def generate_relevant_documents(self):
        """Generate and save a set of Documents relevant to this research session

        :return: The generated set of Documents
        """
        pass


class Page(models.Model):
    """A web page viewed in a ResearchSession."""
    url = models.TextField()
    title = models.TextField()
    content = models.TextField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    document = models.OneToOneField(Document)
    research_session = models.ForeignKey(ResearchSession)


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
