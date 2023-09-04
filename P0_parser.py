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

        # La definición de un procedimiento debe seguir la sintaxis:
        # defProc nomProc(...){
        #    ...
        # }
        # No sé arreglar esto
        if ((tokens[current_token] == ProyecTokens.T_defProc) and (ProyecTokens.T_str in tokens[current_token+1])):
            leftParenthesis = 0
            rightParenthesis = 0
            lBracket = 0
            rBracket = 0
            if (ProyecTokens.T_Lparent not in tokens[current_token+2]):
                print(ProyecTokens.T_Lparent)
                print(tokens[current_token+2])
                print(ProyecTokens.T_Lparent not in tokens[current_token+2])
                print(ProyecTokens.T_Lparent,'not in',tokens[current_token+2])
                valid_program = False
                break
            else:
                leftParenthesis += 1
                while current_token in range(len(tokens)):
                    if current_token == ProyecTokens.T_Lparent:
                        leftParenthesis += 1
                    elif current_token == ProyecTokens.T_Rparent:
                        rightParenthesis += 1
                        # Después del primer paréntesis derecho, debe venir un bracket izquierdo:
                        if (tokens[current_token] == ProyecTokens.T_Rparent) and (tokens[current_token+1] != ProyecTokens.T_Lbracket):
                            valid_program = False
                            break
                        else:
                            lBracket += 1
                            while current_token in range(len(tokens)):
                                if current_token == ProyecTokens.T_Lbracket:
                                    lBracket += 1
                                elif current_token == ProyecTokens.T_Rbracket:
                                    rBracket += 1
                                if lBracket != rBracket:
                                    valid_program = False
                                    break
                    current_token += 1
                if leftParenthesis != rightParenthesis:
                    valid_program = False
                    break
            


        
        current_token += 1

    return valid_program
