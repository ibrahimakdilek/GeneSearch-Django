from django.http import HttpResponse
from django.template import loader 
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status
from rest_framework.views import permissions
from .models import *




def index(request):
    X=Genestudy.objects.filter(approvedsymbol__contains='RGS9')
    context= {
        'listData':[]
    }
    for res in X: 
        context['listData'].append({
            'HGNCID':res.hgncid,
            'ApprovedName':res.approvedname,
            'ApprovedSymbol':res.approvedsymbol,
            'PreviousName':res.previousname,
            'Status':res.status,
            'DateNameChanged':res.datenamechanged,
            'PreviousSymbols':res.previoussymbols,
            'Synonyms':res.synonyms,
            
        })
    template=loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

class CitationDataApi(APIView):
    def get(self,request,*args,**kwargs):
        return Response("asd", status=status.HTTP_200_OK)
