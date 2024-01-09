from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from app.models import *

from app.forms import *

def create_school(request):
    EFSO=SchoolForm()
    d={'EFSO':EFSO}
    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['sname']
            sp=SFDO.cleaned_data['sprincipal']
            sl=SFDO.cleaned_data['slocation']
            e=SFDO.cleaned_data['email']
            re=SFDO.cleaned_data['reenteremail']

            so=School.objects.get_or_create(sname=sn,sprincipal=sp,slocation=sl,email=e,reenteremail=re)[0]
            so.save()
            return HttpResponse('inserting data is done')
        else:
            return HttpResponse('invalid data')
        

    return render(request,'create_school.html',d)
