# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

#from typing_extensions import Self
from django.db import models


class Genestudy(models.Model):
    
    hgncid = models.TextField(db_column='HGNCID', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    approvedname = models.TextField(db_column='ApprovedName', blank=True, null=True)  # Field name made lowercase.
    approvedsymbol = models.TextField(db_column='ApprovedSymbol', blank=True, null=True)  # Field name made lowercase.
    previousname = models.TextField(db_column='PreviousName', blank=True, null=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    datenamechanged = models.TextField(db_column='DateNameChanged', blank=True, null=True)  # Field name made lowercase.
    previoussymbols = models.TextField(db_column='PreviousSymbols', blank=True, null=True)  # Field name made lowercase.
    synonyms = models.TextField(db_column='Synonyms', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GeneStudy'
