from baker_street.models import Document, Question, ResearchSession, Page
from django.contrib import auth
from rest_framework import serializers


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('title', 'url', 'pinned', 'content', 'type', 'source')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question_text', 'document')


class ResearchSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResearchSession
        fields = ('name', 'id', 'current')
        read_only_fields = ('id', 'current')

    def restore_object(self, attrs, instance=None):
        if instance is not None:
            instance.name = attrs.get('name', instance.name)
            return instance
        return ResearchSession(**attrs)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth.get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password', 'groups',
                  'is_active', 'last_login', 'date_joined')
        write_only_fields = ('password',)


class AuthenticationSerializer(serializers.Serializer):
    """
    Base class for authenticating users.
    """
    email = serializers.EmailField()
    password = serializers.CharField()

    def __init__(self, *args, **kwargs):
        self.user_cache = None

        # Copy 'username' field into 'email' field
        if 'data' in kwargs and 'username' in kwargs['data']:
            kwargs['data'] = kwargs['data'].copy()
            kwargs['data']['email'] = kwargs['data']['username']

        super().__init__(*args, **kwargs)

    def validate(self, attrs):
        self.user_cache = auth.authenticate(username=attrs['email'],
                                            password=attrs['password'])
        if self.user_cache is None:
            raise serializers.ValidationError(
                'Please enter a correct email address and password. '
                'Note that both fields may be case-sensitive.',
                code='invalid_login'
            )
        elif not self.user_cache.is_active:
            raise serializers.ValidationError(
                'This account is inactive',
                code='inactive',
            )
        return super().validate(attrs)

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache


class PageSerializer(serializers.ModelSerializer):
    content = serializers.CharField(required=False)

    class Meta:
        model = Page
        fields = ('page_url', 'title', 'content', 'most_recent', 'snippet')
        read_only_fields = ('most_recent',)


class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('url',)
