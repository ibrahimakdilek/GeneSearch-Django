from re import T
from django.http import HttpResponse
from django.template import loader 
from .models import *



def index(request):
    X=Genestudy.objects.filter(approvedsymbol__contains='RGS9')
    context= {
        'listData':[]
    }
    for res in X: 
        context['listData'].append({
            'HGNCID':res.approvedname,
            'Syn':res.synonyms,
            
        })
    template=loader.get_template('index.html')
    return HttpResponse(template.render(context, request))
