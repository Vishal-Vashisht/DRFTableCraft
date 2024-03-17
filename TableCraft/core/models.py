from django.db import models


# Create your models here.
class Connections(models.Model):

    connection_id = models.BigAutoField(primary_key=True)
    connection_name = models.CharField(max_length=50, null=False)
    connection_string = models.CharField(max_length=255, null=False)
    engine = models.CharField(max_length=255, null=False)
    host = models.CharField(max_length=200, null=False)
    port = models.CharField(max_length=200, null=False)
    user = models.CharField(max_length=100, null=False)
    password = models.CharField(max_length=100, null=False)
    db_name = models.CharField(max_length=100, null=False)
