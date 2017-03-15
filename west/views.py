# -*- coding: utf-8 -*-

from django.http import HttpResponse
from west.models import Character

from django.shortcuts import render
from django.core.context_processors import csrf

def first_page(request):
    return HttpResponse("<p>西餐</p>")


# def staff(request):
#    staff_list = Character.objects.all()
#    staff_str  = map(str, staff_list)
#    return HttpResponse("<p>" + ' '.join(staff_str) + "</p>")

# def staff(request):
#    staff_list  = Character.objects.all()
#    staff_str  = map(str, staff_list)
#    context   = {'label': ' '.join(staff_str)}
#    return render(request, 'templay.html', context)

def staff(request):
    staff_list = Character.objects.all()
    return render(request, 'templay.html', {'staffs': staff_list})


def form(request):
    return render(request, 'form.html')


# def investigate(request):
#    rlt = request.GET['staff']
#    return HttpResponse(rlt)

#def investigate(request):
#    ctx = {}
#    ctx.update(csrf(request))
#    if request.POST:
#        ctx['rlt'] = request.POST['staff']
#    return render(request, "investigate.html", ctx)



#def investigate(request):
#    if request.POST:
#        submitted  = request.POST['staff']
#        new_record = Character(name = submitted)
#        new_record.save()
#    ctx ={}
#    ctx.update(csrf(request))
#    all_records = Character.objects.all()
#   ctx['staff'] = all_records
#    return render(request, "investigate.html", ctx)

from django.shortcuts import render
from django.core.context_processors import csrf

from west.models import Character

from django import forms

class CharacterForm(forms.Form):
    name = forms.CharField(max_length = 200)

def investigate(request):
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            submitted  = form.cleaned_data['name']
            new_record = Character(name = submitted)
            new_record.save()

    form = CharacterForm()
    ctx ={}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['staff'] = all_records
    ctx['form']  = form
    return render(request, "investigate.html", ctx)


# from django.http import HttpResponse

def templay(request):
    context = {}
    context['label'] = 'Hello World!'
    return render(request, 'templay.html', context)
