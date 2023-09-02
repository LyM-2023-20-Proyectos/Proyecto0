# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 13:59:58 2023

@author: Lucas Nieto Martínez
@author: 

Lexer
Módulo de análisis léxico del proyecto 0 del curso ISIS-1106: Lenguaje y Máquinas
"""

#----------------------------------------------------
# TOKENS
#----------------------------------------------------
import ProyecTokens
"""
Token: {Tipo, valor opcional}
Clase del objeto token:
"""
class token:
    def __init__(self,type_, value = None):
        self.type = type_
        self.value = value

    # Método de impresión en terminal
    def __printRepr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'
    
#----------------------------------------------------
# ERRORS
#----------------------------------------------------
    
class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Caracter ilegal', details)

#----------------------------------------------------
# Posición
#----------------------------------------------------
class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx  # Índice en el string
        self.ln = ln    # Línea del programa
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)
#----------------------------------------------------
# LEXER
#----------------------------------------------------
class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()

    # Método para avanzar a lo largo del texto:
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None
        
    def makeTokens(self):
        tokens = []
        while self.current_char != None:
            # Ignorar espacios, identación y saltos de línea
            if self.current_char in ' \t':
                self.advance()

            elif self.current_char in ProyecTokens.DIGITS:
                tokens.append(self.makeNumber())
                self.advance()

            elif self.current_char == '{':
                tokens.append(ProyecTokens.T_Lbracket)
                self.advance()

            elif self.current_char == '}':
                tokens.append(ProyecTokens.T_Rbracket)
                self.advance()

            elif self.current_char == '(':
                tokens.append(ProyecTokens.T_Lparent)
                self.advance()

            elif self.current_char == ')':
                tokens.append(ProyecTokens.T_Rparent)
                self.advance()

            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

        return tokens, None
    
    # Dado que la grilla es discreta, no consideraremos tokens para puntos o float numbers
    def makeNumber(self):
        num_str = ''
        while self.current_char != None and self.current_char in ProyecTokens.DIGITS:
            num_str += self.current_char
        self.advance()
        return token(ProyecTokens.T_int,int(num_str))
        
#----------------------------------------------------
# Ejecutar
#----------------------------------------------------

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error
