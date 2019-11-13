import lexer
def main():

    string = '(p and q ifg(r or s)'

    lex = lexer.Lexer(string)
    tokens = lex.tokenisasi()
    print(tokens)
main()