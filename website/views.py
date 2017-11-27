# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import TestCases
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(request, "index.html", {})

def calculator(request):
    vvariation = float(request.POST.get("vvariation"))
    vcontrol = float(request.POST.get("vcontrol"))
    ccontrol = float(request.POST.get("ccontrol"))
    cvariation = float(request.POST.get("cvariation"))
    pvalue = (vvariation*vcontrol)/10
    significance = (ccontrol*cvariation)/5

    t = TestCases(visitor_control=vcontrol, visitor_variation=vvariation,
    conversion_control = ccontrol, conversion_variation = cvariation,
    pvalue = str(pvalue), significance = str(significance),
    )
    t.save()
    # pvalue = 0.01
    # significance = 0.01

    response = {
    "pvalue":pvalue,
    "significance":significance
    }
    print vvariation, vcontrol, ccontrol, cvariation

    return JsonResponse(response)
