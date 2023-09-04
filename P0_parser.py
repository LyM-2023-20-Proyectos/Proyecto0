# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 13:59:58 2023

@author: Lucas Nieto Martínez
@author: 

Lexer
Módulo de análisis gramatical del proyecto 0 del curso ISIS-1106: Lenguaje y Máquinas
Parser True si un programa es válido, de lo contrario retorna false.
"""
import ProyecTokens

#----------------------------------------------------
# Parser
#----------------------------------------------------

def parse_line(tokens):
    # Tokens es la lista de tokens retornada por el lexer
    current_token = 0
    valid_program = True

    while current_token in range(len(tokens)):
        # Una variable o procedimiento sólo puede tener de nombre un string
        if ((tokens[current_token] == ProyecTokens.T_defVar) or (tokens[current_token] == ProyecTokens.T_defProc)) and (ProyecTokens.T_str not in tokens[current_token+1]):
            valid_program = False
            break

        
        # Una variable con nombre sólo puede almacenar un número
        # Si un token es una definición de variable, el siguiente es token string, y el siguiente es token int
        if ((tokens[current_token] == ProyecTokens.T_defVar) and (ProyecTokens.T_str in tokens[current_token+1])):
            if (ProyecTokens.T_int not in tokens[current_token+2]):
                valid_program = False
                break
        
        current_token += 1

    return valid_program
