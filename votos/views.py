# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as asaludaruth_login
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser, User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import *
#meti todos estos imports para que no me salten errores que no entiendo despues


def resultado_global(request):
    """
    Generar la vista para devolver el resultado global de la elección.
    Tener en cuenta que tiene que tener:
    Cantidad total de votos por candidato
    Cantidad total de votos nulos
    Porcentaje de cada candidato
    Porcentaje de votos nulos
    Total de votos de la elección
    """
    context={}
    context['distritos'] = Distrito.objects.all()
    #TODO TU CODIGO AQUI

    return render(request,'global.html',context)


def resultado_distrital(request):
    """
    Generar la vista para devolver el resultado distrital de la elección
    Tener en cuenta que tiene que tener:
    Tamaño del padrón
    Porcentaje de votos del distrito (respecto al padron. Ejemplo: Si el distrito tiene 1000 votantes y hay 750 votos, el porcentaje es 75%)
    Total de votos del distrito
    Candidato ganador
    """
    context={}
    #TODO TU CODIGO AQUI
    
    #context['distrito'] = Distrito.objects.all() / De esta forma no me funciono, lo dejo comentado.
    distrito = Distrito.objects.all()
    
    return render(request,'distrital.html',{'a':distrito})





 #pruebas = Prueba.objects.all()
  #  return render(request, 'index.html', {'todos':pruebas})