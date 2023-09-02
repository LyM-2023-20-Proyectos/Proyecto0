# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 13:59:58 2023

@author: Lucas Nieto Martínez
@author: 
"""

import tokens.py

######################
# TOKENS
######################
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