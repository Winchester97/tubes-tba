import lexer
def main():

    # string = '(p and q ifg(r or s)'
    string = input('Input : ')

    tokens = lexer.Lexer(string).tokenisasi()

    print('Output : '+' '.join([str(token) for token in tokens]))
main()