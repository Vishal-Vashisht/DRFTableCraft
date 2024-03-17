from rest_framework import viewsets
from core.serializer.serializers import ConnectionSerializer
from core.models import Connections
from core.services.database_service import PostgreSQLConfigurator
from core.services.encryption_service import EncryptData

# Create your views here.


class ConnectionsViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Connections.objects.all()
    serializer_class = ConnectionSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data

        pg_db_config = PostgreSQLConfigurator(data)
        encrypter = EncryptData()

        # Encrypt the password and connection string
        encrypted_url = encrypter.encrypt(pg_db_config.db_create_engine())
        encrypt_pass = encrypter.encrypt(data.get("password"))

        # store the encrypted password
        data["connection_string"] = encrypted_url
        data["password"] = encrypt_pass
        serializer.save()
