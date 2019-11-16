from lexer import tokenisasi

def main():
    string = input('Input : ').lower().strip()
    tokens = tokenisasi(string)
    print('Output (Token Lexic) : {0}'.format(' '.join([str(token) for token in tokens])))

main()

