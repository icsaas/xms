# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader,Context,RequestContext
from models import *
from django.utils.translation import ugettext as _
from django import  forms

class PersonForm(forms.Form):
    first=forms.CharField(max_length=100,required=True)
    last=forms.CharField(max_length=100,required=True)
    middle=forms.CharField(max_length=100)

#class LeaderForm(forms.Form):
#    class Meta:
#        model=Leaders



def process_form(request):
    if not request.POST:
        form = PersonForm(initial={'first':'John'})
        return render_to_response('form.html',{'form':form})
    if request.POST:
        post=request.POST.copy()#e.g. {'last':'Doe','first':'John'}
        #form=PersonForm(request.POST)
        form=PersonForm(post)
        print form.first
        return HttpResponseRedirect('/')

def leader_proc(request):
    leaderlist=Leaders.objects.all()
    return {
        'leaderlist':leaderlist
    }

def direction_proc(request):
    directionlist=ResearchDirection.objects.all()
    return {
        'directionlist':directionlist,
    }
def members_proc(request):
    memberlist=Members.objects.all()
    return {
        'memberlist':memberlist
    }


def device_proc(request):
    devicelist=Device.objects.all()
    return {
        'devicelist':devicelist
    }
def labnotice_proc(request):
    labnoticelist=LibNotice.objects.all()
    return {
        'labnoticelist':labnoticelist
    }

def graduate_proc(request):
    graduatelist=Graduate.objects.all()
    return {
        'graduatelist':graduatelist
    }

def index(request):
    Category.objects.filter(title=u'')
    return render_to_response('info/index.html',locals(),context_instance=RequestContext(request,processors=[leader_proc,members_proc,direction_proc]))

def device(request):
    return render_to_response('info/device.html',locals(),context_instance=RequestContext(request,processors=[device_proc]))

def instruction(request):
    return render_to_response('info/instructions.html',locals(),context_instance=RequestContext(request,processors=[labnotice_proc]))

def graduate(request):
    return render_to_response('info/graduate.html',locals(),context_instance=RequestContext(request,processors=[graduate_proc]))















