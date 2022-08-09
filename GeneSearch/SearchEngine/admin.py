from django.contrib import admin

# Register your models here.
from .models import Genestudy


class GeneStudyAdmin(admin.ModelAdmin):
    list_display= ('hgncid', 'approvedname' ,'approvedsymbol', 'datenamechanged', 'previoussymbols', 'synonyms' )
    search_fields= ('hgncid', 'approvedname' ,'approvedsymbol', 'datenamechanged', 'previoussymbols', 'synonyms' )

admin.site.register(Genestudy,GeneStudyAdmin)
