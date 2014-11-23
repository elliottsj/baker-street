from rest_framework import serializers

class CanLIIDocumentSerializer(serializers.Serializer):
    title = serializers.CharField()
    url = serializers.CharField()
