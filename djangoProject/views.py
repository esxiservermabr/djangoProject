import datetime

from django.http import HttpResponse


def bemvindo(request):
    documento = """<html><body><h1>
    Bem vindos, estamos testando a primeira página em Django
    </h1></body></html>"""
    return HttpResponse(documento)


def atemais(request):
    return HttpResponse("Até mais, em breve nos veremos novamente")

def mostratempo(request):

    tempo = datetime.datetime.now()
    hora = tempo.hour
    minuto = tempo.minute
    segundo = tempo.second

    documento = f"""<html><body><h1>
    A hora atual é: {hora}:{minuto}:{segundo}s     
    </h1></body></html>"""

    return HttpResponse(documento)

def idade(request, idadeatual, ano):

    # idadeatual = 40
    periodo = ano - 2022
    idadefutura = idadeatual + periodo

    documento = f"""<html><body><h2>
    Sua idade atual é de: {idadeatual} anos, e no ano de {ano} será de: {idadefutura} anos !!!
    </h2></body></html>"""

    return HttpResponse(documento)