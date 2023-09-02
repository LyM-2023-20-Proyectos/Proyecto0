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
    def __init__(self,type_, value):
        self.type = type_
        self.value = value

    # Método de impresión en terminal
    def __printRepr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'
    
#----------------------------------------------------
# LEXER
#----------------------------------------------------
class Lexer:
    def __init__(self,text):
        self.text = text
        # Variables para recorrer texto:
        self.pos = -1
        self.current_char = None
        self.advance()

    # Método para avanzar a lo largo del texto:
    def advance(self):
        self.pos += 1
        self.current_char = self.text[pos] if self.pos< len(self.text) else None
        
    def makeTokens(self):
        tokens = []
        while self.current_char != None:
            # Ignorar espacios, identación y saltos de línea
            if self.current_char in ' \t':
                self.advance()

            elif self.current_char in ProyecTokens.DIGITS:
                tokens
                self.advance()