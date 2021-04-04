###############################################################
# TOKENS
###############################################################

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'<{self.type}: {self.value}>'
        return f'{self.type}'

###############################################################
# LEX
###############################################################

class Lex:
    def __init__(self):
        # SIGMA
        self.reservewords = ["CHAR", "CONST", "FLOAT", "INT", "VOID", "FOR", "WHILE", "BREAK", "CONTINUE", "IF", "ELSE", "SWITCH", "CASE", "MINE", "CS", "DO", "RETURN", "UOL", "DEAN", "HOD", "#DEFINE", "#INCLUDE"]
        self.identifiers = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
        self.numbers = "0123456789"
        self.operators = ["<", ">", "=", "<>", ":=", "==", "*", "+", "/", "-", ">>>", "<<<", "++", "+=", "-=", "--"]
        self.userio = ["Input", "Output"]
        self.punctuation = ["[", "{", "(", ")", "}", "]", "”"]
        self.double_line_comments = ["/*", "*/"]
        self.single_line_comments = "//"
        # FLAGS
        self.flag_comment = False
        self.flag_string = False
        # Tokens
        self.tokens = []

    def make_token(self, word):
        if word == "":
            return
        #print("|" + word + "|")
        # Checking reserve words
        if word in self.reservewords:
            self.tokens.append(Token("Reserve Word", word))
        # Checking operators
        elif word in self.operators:
            self.tokens.append(Token("Operator", word))
        # Checking punctuation
        elif word in self.punctuation:
            self.tokens.append(Token("Punctuator", word))
        # Checking User I/O
        elif word in self.userio:
            self.tokens.append(Token("User IO", word))
        # Checing Number
        elif word.isdigit():
            self.tokens.append(Token("Digit", word))
        # Checking Floating Point Number
        elif word.count(".") == 1:
            self.tokens.append(Token("Float", word))
        # Checking Identifier
        elif any(i.isdigit() for i in word) and word[-1] != "_":
            self.tokens.append(Token("Identifier", word))
        # Checking String
        elif word[0] == '"' and word[-1] == '"':
            self.tokens.append(Token("String", word))
        else:
            print(" Error! " + "Invalid Word " + word)
            exit()

    def scan(self, filename):
        with open(filename, 'r') as sourcecode:
            lines = sourcecode.read().splitlines()
            for line in lines:
                for word in line.split():
                    if "//" in word:
                        break
                    if "*/" in word:
                        self.flag_comment = False
                        continue
                    if self.flag_comment == True:
                        continue
                    if "/*" in word:
                        self.flag_comment = True
                        continue
                    
                    self.make_token(word)