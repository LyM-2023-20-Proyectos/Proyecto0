# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 13:59:58 2023

@author: Lucas Nieto Martínez
@author: 

Lexer
Módulo de análisis gramatical del proyecto 0 del curso ISIS-1106: Lenguaje y Máquinas
"""
import lexer

#----------------------------------------------------
# Parser
#----------------------------------------------------
class Parser:
    def __init__(self,tokens):
        self.tokens = tokens
        self.tok_index = 1
        self.advance()
    
    def advance(self):
        self.tok_index += 1
        if self.tok_index < len(self.tokens):
            self.current_tok = self.tokens[self.tok_index]
        return self.current_tok
    

    def parse(self):
        res = self.varType()
"""
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