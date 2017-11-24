# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


#EL SUPERUSER ES: admin
#CONTRASEÑA: pepe1234


class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)


    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Candidato(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase:
    
     Decidi ponerle nombre y apellido por razones obvias, y un distrito
    al cual postularse, por lo que esta relacionado con una clave foranea
    """
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    distrito = models.ForeignKey(Distrito)

    
    def __str__(self):
        return 'Nombre: {} {} | Distrito: {}'.format(self.nombre, self.apellido, self.distrito.nombre)

class Votos(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase:, self.candidato_votado.distrito.nombre
    
     En este hice que cada voto este relacionado con un candidato especifico
    mediante una clave foranea, pero tiene la caracteristica de que puede
    ser nulo, osea que no exista dicho voto, o que este en blanco, osea que
    no se halla votado a nadie, pero exista dicho voto, que halla constancia 
    de que se realizo un voto
    """
    candidato_votado = models.ForeignKey(Candidato, null=True, blank=True)
    
    
    def __str__(self):
        return 'Candidato: {} {} | Distrito: {} '.format(self.candidato_votado.nombre, self.candidato_votado.apellido, self.candidato_votado.distrito.nombre)
