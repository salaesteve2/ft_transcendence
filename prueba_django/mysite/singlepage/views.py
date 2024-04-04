from django.shortcuts import render
from django.http import HttpResponse, Http404
from general.views import activate_language
from base.views import torneo_jugar, proximos_torneos

def index(request):
    activate_language(request)
    return render(request, "singlepage/index.html")

def home_section(request):
    activate_language(request)
    jugar = False
    hayProximosTorneos = False
    proximosTorneos = []
    if request.user.is_authenticated:
        res = torneo_jugar(request.user.id)
        jugar = res['ok']
        proximosTorneos = proximos_torneos(request.user.id)
        hayProximosTorneos = (len(proximosTorneos) > 0)
    context = { 'jugar': jugar, 
                    'proximosTorneos': proximosTorneos, 
                    'hayProximosTorneos': hayProximosTorneos }
    return render(request, 'base/home_t.html', context)
