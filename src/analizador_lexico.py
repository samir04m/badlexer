import ply.lex as lex
import os
import codecs

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

palabrasReservadas = (
    "OCUQ", 
    "NOCUQ", 
    "_Y_", 
    "_O_", 
    "NEG" 
    "REPETPR", 
    "REPETMQ", 
    "FIN" 
    "FUN", 
    "DEVOL", 
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
    "SLASH",
    "BACKSLASH"
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
# t_PUNTO = r'\.'
t_PARENTESIS_IZQUIERDO = r'\('
t_PARENTESIS_DERECHO = r'\)'
t_CORCHETE_IZQUIERDO = r'\['
t_CORCHETE_DERECHO = r'\]'
t_LLAVE_IZQUIERDA = r'{'
t_LLAVE_DERECHA = r'}'
#t_SLASH = r'\/"'
t_BACKSLASH = r'\"'

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
    if t.value.lower() in palabrasReservadas:
        print("Se encontro problema")
        t.lexer.skip(1)

    return t

def t_CADENA(t):
   r'\"?(\w+ \ *\w*\d* \ *)\"?'
   return t

def t_NUMERAL(t):
    r'\#'
    return t

def t_MENOR_IGUAL(t):
    r'<='
    return t

def t_MAYOR_IGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
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
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
     r'\*\*(.)*\n'
     t.lexer.lineno += 1
     print("Comentario de una linea")
t_ignore =' \t'

def t_error( t):
    global resultado_lexema
    estado = "** Token no valido en la Linea {:4} Valor {:16} Posicion {:4}".format(str(t.lineno), str(t.value),
                                                                      str(t.lexpos))
    resultado_lexema.append(estado)
    t.lexer.skip(1)



directorio = str(os.getcwd())+"/code/"
archivo =  'test.blur'
directorio = directorio.replace('src/', '')
test = directorio+archivo
print (test)
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()


# Prueba de ingreso
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
#print(cadena)
analizador.input(cadena)

if __name__ == '__main__':
    while True:
        """
        data = input("ingrese: ")
        if data == "q": break
        prueba(data)
        print(resultado_lexema)
        """

        tok = analizador.token()
        if not tok : break
        print (tok)
