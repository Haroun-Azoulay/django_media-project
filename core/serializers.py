from rest_framework import serializers


class PingSerializer(serializers.Serializer):
    message = serializers.CharField()


class VersionSerializer(serializers.Serializer):
    version = serializers.CharField()
