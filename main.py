import lexer
def main():

    # string = '(p and q ifg(r or s)'
    string = input('Input : ')

    lex = lexer.Lexer(string)
    tokens = lex.tokenisasi()

    print('Output : '+' '.join([str(token) for token in tokens]))
main()