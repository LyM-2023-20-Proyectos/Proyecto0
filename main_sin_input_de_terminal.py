import lexer
import P0_parser
import sys

def main():
    file_name = 'validProgram.txt'  # Reemplazar con un txt de otros programas
    with open(file_name, 'r') as file:
        text = file.read()

    tokens, error = lexer.run(file_name, text)
    
    if error:
        print(error.as_string())
        # sys.exit()
    else:
        is_valid_program = P0_parser.parse(tokens)
        if is_valid_program:
            print("El programa es válido.")
            # sys.exit()
        else:
            print("El programa no es válido.")
            # sys.exit()

if __name__ == "__main__":
    main()





