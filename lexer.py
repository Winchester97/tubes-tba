class Lexer(object):

    def __init__(self, string):
        self.string = string
        self.word = ''

    def tokenisasi(self):

        state_pqrs = lambda string : 'error' if (bool(string)) else 1
        state_n = lambda string : state_no(string[1:]) if (string[0]=='o') else 'error'
        state_no = lambda string : state_not(string[1:]) if (string[0]=='t') else 'error'
        state_not = lambda string : 'error' if (bool(string)) else 2
        state_a = lambda string : state_an(string[1:]) if (string[0]=='n') else 'error'
        state_an = lambda string : state_and(string[1:]) if (string[0]=='d') else 'error'
        state_and = lambda string : 'error' if (bool(string)) else 3
        state_o = lambda string : state_or(string[1:]) if (string[0]=='r') else 'error'
        state_or = lambda string : 'error' if (bool(string)) else 4
        state_x = lambda string : state_xo(string[1:]) if (string[0]=='o') else 'error'
        state_xo = lambda string : state_xor(string[1:]) if (string[0]=='r') else 'error'
        state_xor = lambda string : 'error' if (bool(string)) else 5
        state_i = lambda string : state_if(string[1:]) if (string[0]=='f') else 'error'
        state_if = lambda string : cek_iff(string) if (bool(string)) else 6
        cek_iff = lambda string : state_iff(string[1:]) if (string[0]=='f') else 'error'
        state_iff = lambda string : 'error' if (bool(string)) else 8
        state_t = lambda string : state_th(string[1:]) if (string[0]=='h') else 'error'
        state_th = lambda string : state_the(string[1:]) if (string[0]=='e') else 'error'
        state_the = lambda string : state_then(string[1:]) if (string[0]=='n') else 'error'
        state_then = lambda string : 'error' if (bool(string)) else 7
        state_bukakurung = lambda : 9
        state_tutupkurung = lambda : 10

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
