#!/usr/bin/env python

class Tipo :

    def __init__(self, nombre):
        self.nombre = nombre

    def get(self):
        print ("Tipo : ", self.nombre)

    def getNombre(self):
        return self.nombre