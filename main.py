import lexer

def main():
    
    while True:
        text = input('basic > ')
        result, error = basic.run('<stdin>', text)

        if error:
            print(error.as_string())
        else:
            print(result)


if __name__ == '__main__':
    main()