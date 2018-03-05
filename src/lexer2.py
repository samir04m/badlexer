#!/usr/bin/env python
import ply.lex as lex
import re
import codecs
import os
import sys

import token2
import tipo


identifier = tipo.Tipo("Identificador")
assignation = tipo.Tipo("Asignacion")
keyword = tipo.Tipo("Palabra Reservada")
separator = tipo.Tipo("Separador")
operator = tipo.Tipo("Operador")
literal = tipo.Tipo("Literal")
comment = tipo.Tipo("Comentario")

tokens = [  
            #Operador de asignaciones
            token2.Token("::", assignation),

            #Palabras Reservadas
            token2.Token("_most", keyword),
            token2.Token("_obt", keyword),
            token2.Token("ocuq", keyword),
            token2.Token("nocuq", keyword),
            token2.Token("f>", keyword),
            token2.Token("repetmq", keyword),
            token2.Token("proc", keyword),
            token2.Token("fp", keyword),
            token2.Token("devol", keyword),

            #Separadores
            token2.Token("ent", separator),
            token2.Token("hac", separator),
            token2.Token("(", separator),
            token2.Token(")", separator),
            token2.Token("{", separator),
            token2.Token("}", separator),
            token2.Token(",", separator),

            #Operadores aritmeticos y logicos
            token2.Token("+", operator),
            token2.Token("-", operator),
            token2.Token("*", operator),
            token2.Token("/", operator), 
            token2.Token("%", operator), 
            token2.Token("^", operator),
            token2.Token("<", operator),
            token2.Token(">", operator),
            token2.Token("<=", operator),
            token2.Token(">=", operator),

            #Literales
            token2.Token("\"", literal),
            token2.Token("\'", literal),
            token2.Token("v", literal),
            token2.Token("f", literal),
]
"""
for token2 in tokens:
    token2.get()
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

tokenList = []
for token in tokens :
    tokenList.append(token.getLexema())

def t_ID(t):
    r'[>_][a-zA-Z][a-zA-Z0-9_]*'
    if t.value in tokenList:
        t.type = t.value
    
    return t

def t_COMMENT(t):
    r'<<<.*.>>>'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value) 


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
     r'\/\/(.)*\n'
     t.lexer.lineno += 1
     print("Comentario de una linea")

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

directorio = str(os.getcwd())+"/code/"
archivo =  'program.unimag'
directorio = directorio.replace('src/', '')
test = directorio+archivo
print (test)
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()


#analizador = lex.lex()

#analizador.input(cadena)

def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)

    resultado_lexema.clear()
    while True:
        tok = analizador.token()
        if not tok:
            break
        # print("lexema de "+tok.type+" valor "+tok.value+" linea "tok.lineno)
        estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno),str(tok.type) ,str(tok.value), str(tok.lexpos) )
        resultado_lexema.append(estado)
    return resultado_lexema

 # instanciamos el analizador lexico
analizador = lex.lex()
analizador.input(cadena)

if __name__ == '__main__':
    while True:
        """
        data = input("ingrese: ")
        prueba(data)
        print(resultado_lexema)
        """
        
  
        tok = analizador.token()
        if not tok : break
        print (tok)
        

