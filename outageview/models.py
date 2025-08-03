from django.db import models

# Create your models here.
from django.db import models

class ActiveOutage(models.Model):
    outage_number = models.CharField(primary_key=True, max_length=100, unique=True)  # ✅ Set as PK
    description = models.TextField()
    area = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    customers_affected = models.IntegerField()
    eta = models.DateTimeField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'active_outages'  # Use your existing table

class ArchiveOutage(models.Model):
    outage_number = models.CharField(primary_key=True, max_length=100, unique=True)  # ✅ Set as PK
    description = models.TextField()
    area = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    customers_affected = models.IntegerField()
    eta = models.DateTimeField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'archive_outages'
