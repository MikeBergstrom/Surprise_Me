# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
VALUES = ['Look at this random thing', 'potato', 'This is a crazy string', 'Randommmmmmm', 'Randumb',"Didn't see this one coming!"]



def index(request):
    return render(request, 'surprise/index.html')

def process(request):
    request.session['surprises'] = []
    if request.method == "POST":
        print request.POST['number']
        for i in range(0, int(request.POST['number'])):
            request.session['surprises'].append(random.choice(VALUES))
    print request.session['surprises']
    return redirect('/results')


def results(request):
    print "in results"
    print request.session['surprises']
    return render(request, 'surprise/results.html')
    pass


# Create your views here.
