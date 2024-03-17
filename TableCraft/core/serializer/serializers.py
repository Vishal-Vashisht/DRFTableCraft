from rest_framework import serializers
from core.models import Connections


class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Connections
        fields = ['url', 'connection_name',
                  'engine', 'host',
                  'port', 'user',
                  'db_name', "password"]

    def validate_connection_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("Connection names must be 4 character")
