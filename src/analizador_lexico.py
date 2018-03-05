import ply.lex as lex
import os
import codecs
"""
reservada = (
    # Palabras Reservadas
    'FUN',
    'USING',
    'NAMESPACE',
    'STD',
    'COUT',
    'CIN',
   'GET',
   'CADENA',
  'RETURN',
   'VOID',
    'INT',
    'ENDL',
)
"""
palabrasReservadas = (
    "OCUQ", 
    "NOCUQ", 
    "_Y_", 
    "_O_", 
    "NEG", 
    "REPETPR", 
    "REPETMQ", 
    "FIN", 
    "FUN", 
    "DEVOL"
)
tiposDeToken = (
    "IDENTIFICADOR",
    "PALABRA_RESERVADA",
    "OPERADOR",
    "DELIMITADOR",
    "LITERAL"
)

tokens = tiposDeToken + (
    "ENTERO",
    "CADENA",
    "NUMERAL",
    "MENOR_IGUAL",
    "MAYOR_IGUAL",
    "IGUAL",
    "DIFERENTE",
    "ASIGNACION",
    "SUMA",
    "RESTA",
    "MULTIPLICACION",
    "DIVISION",
    "MODULO",
    "POTENCIA",
    "AND",
    "OR",
    "NOT",
    "MENOR_QUE",
    "MAYOR_QUE",
    "PUNTO_COMA",
    "COMA",
    "PUNTO",
    "PARENTESIS_IZQUIERDO",
    "PARENTESIS_DERECHO",
    "CORCHETE_IZQUIERDO",
    "CORCHETE_DERECHO",
    "LLAVE_IZQUIERDA",
    "LLAVE_DERECHA",
    "BACKSLASH",
    "COMILLA_DOBLE",
    "COMILLA_SIMPLE",
    "V",
    "F"
)
"""
tokens = reservada + (
    'IDENTIFICADOR',
    'ENTERO',
    'ASIGNACION',

    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',

   'MINUSMINUS',
   'PLUSPLUS',

    #Condiones
   'OCUQ',
    'SINO',
    #Ciclos
   'MIENTRAS',
   'PARA',
    #logica
    'AND',
    'OR',
    'NOT',
    'MENORQUE',
    'MENORIGUAL',
    'MAYORQUE',
    'MAYORIGUAL',
    'IGUAL',
    'DIFERENTE',
    # Symbolos
    'NUMERAL',

    'PARIZQ',
    'PARDER',
    'CORIZQ',
    'CORDER',
    'LLAIZQ',
    'LLADER',
    
    # Otros
    'PUNTOCOMA',
    'COMA',
    'COMDOB',
    'MAYORDER', #>>
    'MAYORIZQ', #<<

    'ID',
    'KEYWORD',
    "PALABRA_RESERVADA",
)
"""
t_ignore =' \t'
t_ASIGNACION = r'::'

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'

t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENOR_QUE = r'<'
t_MAYOR_QUE = r'>'
t_PUNTO_COMA = ';'
t_COMA = r','
t_PUNTO = r'\.'
t_PARENTESIS_IZQUIERDO = r'\('
t_PARENTESIS_DERECHO = r'\)'
t_CORCHETE_IZQUIERDO = r'\['
t_CORCHETE_DERECHO = r'\]'
t_LLAVE_IZQUIERDA = r'{'
t_LLAVE_DERECHA = r'}'
t_BACKSLASH = r'\\'
t_COMILLA_SIMPLE = r'\''
t_COMILLA_DOBLE = r'\"'

def t_PALABRA_RESERVADA(t):
    r'[A-Z][A-Z][A-Z]+'
    if t.value in palabrasReservadas:
        t.type = 'PALABRA_RESERVADA'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    #r'[a-zA-Z][a-zA-Z0-9_]*'
    if t.value.upper() in palabrasReservadas:
        invalido(t,'Es una palabra reservada')
    else:
        return t

def t_CADENA(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t

def t_NUMERAL(t):
    r'\#'
    return t

def t_MENOR_IGUAL(t):
    r'<::'
    return t

def t_MAYOR_IGUAL(t):
    r'>::'
    return t

def t_IGUAL(t):
    r':::'
    return t

def t_DIFERENTE(t):
    r':-:'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'\*\*\*(.|\n)*?\*\*\*'
    t.lexer.lineno += t.value.count('\n')
    print("Linea %d inicia comentario de multiples lineas"%(t.lineno))

def t_comments_ONELine(t):
     r'\*\*(.)*\n'
     t.lexer.lineno += 1
     print("Linea %d comentario"%(t.lineno))

def t_error(t):
    print("Linea %d -> Token %r invalido." % (t.lineno, t.value) )
    print("-------------------------------------------------------")
    t.lexer.skip(1)    
    
def invalido(t, arg='Error Indefinido'):
    print("Linea %d -> Token %r invalido." % (t.lineno, t.value) )
    if arg : print("Descripcion del error :", arg)
    print("-------------------------------------------------------")


directorio = str(os.getcwd())+"/code/"
nombreArchivo =  'test.blur'
directorio = directorio.replace('src/', '')
ruta = directorio+nombreArchivo
print (ruta)
fp = codecs.open(ruta,"r","utf-8")
codigoArchivo = fp.read()
fp.close()

analizadorLexico = lex.lex()
#print(codigoArchivo)
analizadorLexico.input(codigoArchivo)

if __name__ == '__main__':
    while True:
        tkn = analizadorLexico.token()
        if not tkn : break
        print (tkn)
