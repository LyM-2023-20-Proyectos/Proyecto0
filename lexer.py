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
# Errores
#----------------------------------------------------
    
class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.file_name}, line {self.pos_start.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Caracter ilegal', details)

#----------------------------------------------------
# Posición
#----------------------------------------------------
class Position:
    def __init__(self, idx, ln, col, file_name, ftxt):
        self.idx = idx  # Índice en el string
        self.ln = ln    # Línea del programa
        self.col = col
        self.file_name = file_name
        self.ftxt = ftxt

    def advance(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.file_name, self.ftxt)
#----------------------------------------------------
# LEXER
#----------------------------------------------------
class Lexer:
    def __init__(self, file_name, text):
        self.file_name = file_name
        self.text = text
        self.pos = Position(-1, 0, -1, file_name, text)
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

            elif self.current_char in '1234567890':
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
            
            elif self.current_char == ',':
                tokens.append(ProyecTokens.T_comma)
                self.advance()

            elif self.current_char == ';':
                tokens.append(ProyecTokens.T_semiColon)
                self.advance()

            # Definición de variables o procedimientos, lenguaje del robot no distingue entre upper case o lower case
            elif (self.current_char == 'd' or self.current_char == 'D'):
                self.advance()
                if (self.current_char == 'e' or self.current_char == 'E'):
                    self.advance()
                    if (self.current_char == 'f' or self.current_char == 'F'):
                        self.advance()
                # A partir de este punto, la definición puede ser una variable o un procedimiento
                        if (self.current_char == 'v' or self.current_char == 'V'):
                            self.advance()
                            if (self.current_char == 'a' or self.current_char == 'A'):
                                self.advance()
                                if (self.current_char == 'r' or self.current_char == 'R'):
                                    tokens.append(ProyecTokens.T_defVar)
                                    self.advance()
                        elif (self.current_char == 'p' or self.current_char == 'P'):
                            self.advance()
                            if (self.current_char == 'r' or self.current_char == 'R'):
                                self.advance()
                                if (self.current_char == 'o' or self.current_char == 'O'):
                                    self.advance()
                                    if (self.current_char == 'c' or self.current_char == 'C'):
                                        tokens.append(ProyecTokens.T_defProc)
                                        self.advance()

            # Condicionales
            elif (self.current_char == 'i' or self.current_char == 'I'):
                self.advance()
                if (self.current_char == 'f' or self.current_char == 'F'):
                    tokens.append(ProyecTokens.T_ifCon)
                    self.advance()

            elif (self.current_char == 'e' or self.current_char == 'E'):
                self.advance()
                if (self.current_char == 'l' or self.current_char == 'L'):
                    self.advance()
                    if (self.current_char == 's' or self.current_char == 'S'):
                        self.advance()
                        if (self.current_char == 'e' or self.current_char == 'E'):
                            tokens.append(ProyecTokens.T_elseCon)
                            self.advance()

            # Ciclos
            elif (self.current_char == 'w' or self.current_char == 'W'):
                self.advance()
                if (self.current_char == 'h' or self.current_char == 'H'):
                    self.advance()
                    if (self.current_char == 'i' or self.current_char == 'I'):
                        self.advance()
                        if (self.current_char == 'l' or self.current_char == 'L'):
                            self.advance()
                            if (self.current_char == 'e' or self.current_char == 'E'):
                                tokens.append(ProyecTokens.T_while)
                                self.advance()

            # Condiciones
            elif (self.current_char == 'c' or self.current_char == 'C'):
                self.advance()
                if (self.current_char == 'a' or self.current_char == 'A'):
                    self.advance()
                    if (self.current_char == 'n' or self.current_char == 'N'):
                        tokens.append(ProyecTokens.T_can)
                        self.advance()

            elif (self.current_char == 'n' or self.current_char == 'N'):
                self.advance()
                if (self.current_char == 'o' or self.current_char == 'O'):
                    self.advance()
                    if (self.current_char == 't' or self.current_char == 'T'):
                        tokens.append(ProyecTokens.T_not)
                        self.advance()
                        
            elif (self.current_char == 'f' or self.current_char == 'F'):
                self.advance()
                if (self.current_char == 'a' or self.current_char == 'A'):
                    self.advance()
                    if (self.current_char == 'c' or self.current_char == 'C'):
                        self.advance()
                        if (self.current_char == 'i' or self.current_char == 'I'):
                            self.advance()
                            if (self.current_char == 'n' or self.current_char == 'N'):
                                self.advance()
                                if (self.current_char == 'g' or self.current_char == 'G'):
                                    tokens.append(ProyecTokens.T_facing)
                                    self.advance()

            # Comando de repetir bloques de código n veces
            elif (self.current_char == 'r' or self.current_char == 'R'):
                self.advance()
                if (self.current_char == 'e' or self.current_char == 'E'):
                    self.advance()
                    if (self.current_char == 'p' or self.current_char == 'P'):
                        self.advance()
                        if (self.current_char == 'e' or self.current_char == 'E'):
                            self.advance()
                            if (self.current_char == 'a' or self.current_char == 'A'):
                                self.advance()
                                if (self.current_char == 't' or self.current_char == 'T'):
                                    tokens.append(ProyecTokens.T_repeat)
                                    self.advance()

            elif (self.current_char == 't' or self.current_char == 'T'):
                self.advance()
                if (self.current_char == 'i' or self.current_char == 'I'):
                    self.advance()
                    if (self.current_char == 'm' or self.current_char == 'M'):
                        self.advance()
                        if (self.current_char == 'e' or self.current_char == 'E'):
                            self.advance()
                            if (self.current_char == 's' or self.current_char == 'S'):
                                tokens.append(ProyecTokens.T_times)
                                self.advance()
            
            #Comandos simples
            elif (self.current_char == 'w' or self.current_char == 'W'):
                self.advance()
                if (self.current_char == 'a' or self.current_char == 'A'):
                    self.advance()
                    if (self.current_char == 'l' or self.current_char == 'L'):
                        self.advance()
                        if (self.current_char == 'k' or self.current_char == 'K'):
                            tokens.append(ProyecTokens.T_walk)
                            self.advance()
            elif (self.current_char == 'g' or self.current_char == 'G'):
                self.advance()
                if (self.current_char == 'r' or self.current_char == 'R'):
                    self.advance()
                    if (self.current_char == 'a' or self.current_char == 'A'):
                        self.advance()
                        if (self.current_char == 'b' or self.current_char == 'B'):
                            tokens.append(ProyecTokens.T_grab)
                            self.advance()
            elif (self.current_char == 'd' or self.current_char == 'D'):
                self.advance()
                if (self.current_char == 'r' or self.current_char == 'R'):
                    self.advance()
                    if (self.current_char == 'o' or self.current_char == 'O'):
                        self.advance()
                        if (self.current_char == 'p' or self.current_char == 'P'):
                            tokens.append(ProyecTokens.T_drop)
                            self.advance()
                            


            # Las variables o procedimientos deben tener nombres
            elif self.current_char in 'abcdefghijklmnopqrstuvwxyz_-ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                tokens.append(self.makeName())
                self.advance()

            # Caractéres que no están en el alfabeto
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

        return tokens, None
    
    # Dado que la grilla es discreta, no consideraremos tokens para puntos o float numbers
    def makeNumber(self):
        num_str = ''

        while self.current_char != None and self.current_char in '1234567890':
            num_str += self.current_char
            self.advance()

        return f'{ProyecTokens.T_int}:{num_str}'
    
    def makeName(self):
        name_str = ''
        while self.current_char != None and self.current_char in 'abcdefghijklmnopqrstuvwxyz_-ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            name_str += self.current_char
            self.advance()

        return f'{ProyecTokens.T_str}:{name_str}'



#----------------------------------------------------
# Nodos
#----------------------------------------------------

class NumberNode:

    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f'{self.token}'
    
class BinaryOperationNode:
    def __init__(self, funcType, varName, factor):
        self.funcType = funcType
        self.varName = varName
        self.factor = factor
    
    def __repr__(self):
        return f'{self.funcType}',f'{self.varName}',f'{self.factor}'

#----------------------------------------------------
# Parser
#----------------------------------------------------
"""
class Parser:
    def __init__(tokens):
        self.tokens = tokens
        self.tok_index = 1
        self.advance()
    
    def advance():
        self.tok_index += 1
        if self.tok_index < len(self.tokens):
            self.current_tok = self.tokens[self.tok_index]
        return self.current_tok
    

    def parse(self):
        res = self.varType()

    def factor(self):
        tok = self.current_factor

        if tok.type in (ProyecTokens.T_int, ProyecTokens.T_str):
            self.advance()
            return NumberNode(tok)
        
    def nombre(self):
        if token.type in (ProyecTokens.T_name):
            self.advance()
            return NumberNode(token)

    def varType(self):
        if token.type in (ProyecTokens.T_defVar, ProyecTokens.T_defProc):
            return NumberNode(token)
"""
#----------------------------------------------------
# Ejecutar
#----------------------------------------------------

def run(file_name, text):
    #Tokens
    lexer = Lexer(file_name, text)
    tokens, error = lexer.makeTokens()
    if error: return None, error

    #Abstract Synthax Tree
    # parser = Parser(tokens)
    # ast = parser.parse()

    return tokens, error
