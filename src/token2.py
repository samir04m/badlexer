#!/usr/bin/env python

from __future__ import print_function

class Token:

    def __init__(self, lexema, tipo):
        self.lexema = lexema
        self.tipo = tipo

    def get(self):
        print ("Lexema:", self.lexema)
        print ("\tTipo:", self.tipo.getNombre())

    def getLexema(self):
        return self.lexema

    def getTipo(self):
        return self.tipo.getNombre()