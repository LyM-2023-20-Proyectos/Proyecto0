import lexer

def main():
    
    while True:
        text = input('Texto del programa> ')
        result, error = lexer.run('<stdin>', text)

        if error:
            print(error.as_string())
        else:
            print(result)


if __name__ == '__main__':
    main()