#!/usr/bin/env python
import token
import tipo

import ply.ply.lex as lex
import os
import re
import codecs
import sys


identifier = tipo.Tipo("Identificador")
assignation = tipo.Tipo("Asignacion")
keyword = tipo.Tipo("Palabra Reservada")
separator = tipo.Tipo("Separador")
operator = tipo.Tipo("Operador")
literal = tipo.Tipo("Literal")
comment = tipo.Tipo("Comentario")

tokens = [  
            #Operador de asignaciones
            token.Token("::", assignation),

            #Palabras Reservadas
            token.Token("_most", keyword),
            token.Token("_obt", keyword),
            token.Token("ocuq", keyword),
            token.Token("nocuq", keyword),
            token.Token("f>", keyword),
            token.Token("repetmq", keyword),
            token.Token("proc", keyword),
            token.Token("fp", keyword),
            token.Token("devol", keyword),

            #Separadores
            token.Token("ent", separator),
            token.Token("hac", separator),
            token.Token("(", separator),
            token.Token(")", separator),
            token.Token("{", separator),
            token.Token("}", separator),
            token.Token(",", separator),

            #Operadores aritmeticos y logicos
            token.Token("+", operator),
            token.Token("-", operator),
            token.Token("*", operator),
            token.Token("/", operator), 
            token.Token("%", operator), 
            token.Token("^", operator),
            token.Token("<", operator),
            token.Token(">", operator),
            token.Token("<=", operator),
            token.Token(">=", operator),

            #Literales
            token.Token("\"", literal),
            token.Token("\'", literal),
            token.Token("v", literal),
            token.Token("f", literal),
]
"""
for token in tokens:
    token.get()
"""    
t_ignore = " \t"
t_NOMBRE = r'[>_][a-zA-Z][a-zA-Z0-9_]*'

t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'\^'
t_ASIGNAR = r'::'
   
t_AND = r'\_\Y\_'
t_OR = r'\_\O\_'
t_NOT = r'\n\e\g'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_COMDOB = r'\"'

def t_ID(t):
    r'[>_][a-zA-Z][a-zA-Z0-9_]*'
    if t.value in tokens.lexema:
        t.type = t.value
    
    return t

def t_COMMENT(t):
    r'\<<<.*.\>>>'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value) 


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print ("Caracter invalido ", t.value[0])
    t.lexer.sikip(1)
"""
def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print str(cont)+". "+files
        cont = cont+1

    while respuesta == False:
        numArchivo == raw_input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break
    
    print ("Has escogido ", files[int(numArchivo)-1])

    return files[int(numArchivo)-1]
"""

print (str(os.getcwd())+"/code/")
directorio = str(os.getcwd())+"/code/"

archivo =  'program.unimag'
test = directorio+archivo
print (test)
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)
"""
while True:
    tok = analizador.token()
    if not tok : break
    print tok
"""

