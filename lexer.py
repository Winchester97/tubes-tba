class Lexer(object):

    def __init__(self, string):
        self.string = string
        self.word = ''

    def tokenisasi(self):

        def state_pqrs(string):
            if bool(string): return 'error'
            else: return 1

        def state_n(string):
            if(string[0] == 'o'): return state_no(string[1:])
            else: return 'error'
        def state_no(string):
            if(string[0] == 't'): return state_not(string[1:])
            else: return 'error'
        def state_not(string):
            if bool(string): return 'error'
            else: return 2

        def state_a(string):
            if(string[0] == 'n'): return state_an(string[1:])
            else: return 'error'
        def state_an(string):
            if(string[0] == 'd'): return state_and(string[1:])
            else: return 'error'
        def state_and(string):
            if bool(string): return 'error'
            else: return 3

        def state_o(string):
            if(string[0] == 'r'): return state_or(string[1:])
            else: return 'error'
        def state_or(string):
            if bool(string): return 'error'
            else: return 4

        def state_x(string):
            if(string[0] == 'o'): return state_xo(string[1:])
            else: return 'error'
        def state_xo(string):
            if(string[0] == 'r'): return state_xor(string[1:])
            else: return 'error'
        def state_xor(string):
            if bool(string): return 'error'
            else: return 5

        def state_i(string):
            if(string[0] == 'f'): return state_if(string[1:])
            else: return 'error'
        def state_if(string):
            if bool(string):
                if(string[0] == 'f'): return state_iff(string[1:])
                else: return 'error'
            else: return 6
        def state_iff(string):
            if bool(string): return 'error'
            else: return 8

        def state_t(string):
            if(string[0] == 'h'): return state_th(string[1:])
            else: return 'error'
        def state_th(string):
            if(string[0] == 'e'): return state_the(string[1:])
            else: return 'error'
        def state_the(string):
            if(string[0] == 'n'): return state_then(string[1:])
            else: return 'error'
        def state_then(string):
            if bool(string): return 'error'
            else: return 7

        def state_bukakurung():
            return 9
        def state_tutupkurung():
            return 10

        def state_initial(string):
            proposisi = ['p','q','r','s']
            char = string[0]
            if (char in proposisi): return state_pqrs(string[1:])
            elif (char == 'n'): return state_n(string[1:])
            elif (char == 'a'): return state_a(string[1:])
            elif (char == 'o'): return state_o(string[1:])
            elif (char == 'x'): return state_x(string[1:])
            elif (char == 'i'): return state_i(string[1:])
            elif (char == 't'): return state_t(string[1:])
            elif (char == '('): return state_bukakurung()
            elif (char == ')'): return state_tutupkurung()
            else: return 'error'

        tokens = []

        def input_token(string):
            token = state_initial(string)
            tokens.append(token)
            if token == 'error': return False
            self.word = ''

        for i, char in enumerate(self.string):
            string = self.word
            if char != ' ':
                if (char == '('):
                    if (bool(string) and (input_token(string) is False)): break
                    if (input_token(char) is False): break
                elif char == ')':
                    if (bool(string) and (input_token(string) is False)): break
                    if (input_token(char) is False): break
                else:
                    self.word += char
                if (i+1 == len(self.string)) and (char!='(' and char!=')'):
                    string = self.word
                    if (input_token(string) is False): break
            else:
                if (input_token(string) is False): break

        return tokens
